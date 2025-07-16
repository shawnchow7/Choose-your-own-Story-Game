# import uuid for generating unique identifiers
import uuid

from typing import Optional
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from db.database import get_db, SessionLocal
from models.story import Story, StoryNode
from models.job import StoryJob
from schemas.story import(
    CompleteStoryResponse, CompleteStoryNodeResponse, CreateStoryRequest
)
from schemas.job import StoryJobResponse
from core.story_generator import StoryGenerator

router = APIRouter(
    prefix='/stories',
    tags=['stories'],
)


# session will identify your browser when you are interacting with a website
# will look for a session id in the browser cookies
def get_session_id(session_id: Optional[str] = Cookie(None)):
    if not session_id:
        # if no session id, create a new one
        session_id = str(uuid.uuid4())
    return session_id


# creates a POST end point , the url path is "/create"
# format the response using this schema
@router.post("/create",response_model=StoryJobResponse)
def create_story(
    # validates the request body against the CreateStoryRequest schema
    # if fail it will return a 400 error
    request: CreateStoryRequest,
    # for running task after the response is sent
    background_tasks: BackgroundTasks,
    response: Response,

    # get the session id from the cookie, if not present it will create a new one
    session_id: str = Depends(get_session_id),
    db: Session = Depends(get_db)
):
    # set a cookie in the response with the session id
    # httponly means it can't be accessed by JavaScript, only by the server
    response.set_cookie(key="session_id", value=session_id, httponly=True)

    # create a new job id
    # this is a unique identifier for the job
    job_id = str(uuid.uuid4())

    # create a new job in the database
    # creates a job object with the job_id, status, theme, and session_id
    job= StoryJob(
        job_id=job_id,
        status="pending",
        theme=request.theme,
        session_id=session_id
    )

    # add the job to the database session
    db.add(job)
    # commit the session to save the job in the database
    db.commit()

    # after you send the response, run this function in the backgrodund
    # this function will run after the user gets the response
    # and it will generate the story in the background
    # by using a new thread
    background_tasks.add_task(generate_story_task, 
                              job_id=job_id, 
                              theme=request.theme, 
                              session_id=session_id)

    return job

def generate_story_task(job_id: str, theme: str, session_id: str):

    db = SessionLocal()
    try:
        job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()

        if not job:
            return
        
        try:
            job.status = "processing"
            db.commit()

            print(f"Starting story generation for job {job_id} with theme {theme}")
            story = StoryGenerator.generate_story(db, session_id, theme)
            print(f"Story generated successfully with ID {story.id}")

            job.story_id = story.id
            job.status = "completed"
            job.completed_at = datetime.now()
            db.commit()
            print(f"Job {job_id} completed successfully")

        except Exception as e:
            print(f"Error in story generation: {str(e)}")
            import traceback
            traceback.print_exc()
            job.status = "failed"
            job.error = str(e)
            job.completed_at = datetime.now()
            db.commit()

    finally:
        db.close()
    

@router.get("/{story_id}", response_model=CompleteStoryResponse)
def get_story(story_id:int, db: Session = Depends(get_db)):
    story = db.query(Story).filter(Story.id == story_id).first()
    
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    
    complete_story= build_complete_story_tree(db, story)
    return complete_story
    
    

    # build the complete story tree
    # that can be accessed by the frontend
def build_complete_story_tree(db: Session, story:Story) -> CompleteStoryResponse:
    nodes = db.query(StoryNode).filter(StoryNode.story_id == story.id).all()

    node_dict = {}
    for node in nodes:
        node_response = CompleteStoryNodeResponse(
            id=node.id,
            content=node.content,
            is_ending=node.is_ending,
            is_winning_ending=node.is_winning,
            options=node.option or []
        )
        node_dict[node.id] = node_response

    root_node = next((node for node in nodes if node.is_root), None)
    if not root_node:
        raise HTTPException(status_code=500, detail="Story root node not found")

    return CompleteStoryResponse(
        id=story.id,
        title= story.title,
        session_id=story.session_id,
        created_at=story.created_at,
        root_node=node_dict[root_node.id],
        all_nodes=node_dict
    )
    
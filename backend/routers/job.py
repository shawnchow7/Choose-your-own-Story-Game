import uuid 
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Cookie, Response, BackgroundTasks
from sqlalchemy.orm import Session

from db.database import get_db
from models.job import StoryJob
from schemas.job import StoryJobResponse

router = APIRouter(
    prefix='/jobs',
    tags=['jobs'],
)

@router.get("/{job_id}", response_model=StoryJobResponse)
def get_job_status(job_id: str, db: Session = Depends(get_db)):
    # Fetch the job from the database using the job_id
    job = db.query(StoryJob).filter(StoryJob.job_id == job_id).first()
    
    # If no job found, raise a 404 error
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    # Return the job details as a response
    return job

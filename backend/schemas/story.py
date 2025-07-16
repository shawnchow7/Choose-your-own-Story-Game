from typing import List, Optional, Dict  
from pydantic import BaseModel
from datetime import datetime

#schema to define the structure of the data the api will accept and return
# and then pydantic will validate the data against this schema

class StoryOptionsSchema(BaseModel):
    text: str
    node_id : Optional[int] = None

# base => not going to be used directly in api, but will be inherited by other schemas
class StoryNodeBase(BaseModel):
    content:str
    is_ending: bool = False
    is_winning_ending : bool = False


# response => what the response from the api will look like
class CompleteStoryNodeResponse(StoryNodeBase):
    id:int
    options: List[StoryOptionsSchema] = []

    class Config:
        from_attributes = True

class StoryBase(BaseModel):
    title: str
    session_id: Optional[str] = None

    class Config:
        from_attributes = True

class CreateStoryRequest(BaseModel):
    theme: str

class CompleteStoryResponse(StoryBase):
    id: int
    created_at: datetime
    root_node: CompleteStoryNodeResponse
    all_nodes: Dict[int, CompleteStoryNodeResponse]


    class Config:
        from_attributes = True

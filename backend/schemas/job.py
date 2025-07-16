from typing import Optional, List

# for datetime handling
from datetime import datetime

# BaseModel pydantic class for creating data validation schemas
from pydantic import BaseModel

# This file defines Pydantic schemas - 
# these are like data contracts that define what data looks like when it goes in and out of your API. 
# They're different from your database models.

class StoryJobBase(BaseModel):
    theme: str
  
class StoryJobResponse(BaseModel):
    job_id: str
    status: str
    created_at: datetime
    # this field is either int or None
    story_id: Optional[int] = None
    completed_at: Optional[datetime] = None
    error: Optional[str] = None

    class Config: 
        # from_attributes = True: 
        # Allows Pydantic to convert SQLAlchemy database objects into these schemas
        from_attributes = True

class StoryJobCreate(StoryJobBase):
    pass
 
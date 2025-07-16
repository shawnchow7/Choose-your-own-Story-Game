# as story takes a couple of time to create story by llm
# when someone creates a story, it will take some time to create the story nodes
# job is going to represent the intent to create a story

# job to tell us status of the story creation

# tools to define database columns and their types
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,Boolean,JSON

# creates connections between different tables
from sqlalchemy.orm import relationship

# to get the current time
from sqlalchemy.sql import func

from db.database import Base

class StoryJob(Base):
    __tablename__ = 'story_jobs'

    id = Column(Integer, primary_key=True, index=True)

    job_id = Column(String, index=True, unique=True)

    session_id = Column(String, index=True)

    theme = Column(String, index=True)

    status = Column(String, index=True)

    story_id = Column(Integer, nullable=True)

    error = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    completed_at = Column(DateTime(timezone=True), nullable=True)
    
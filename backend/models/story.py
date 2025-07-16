# tools to define database columns and their types
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,Boolean,JSON

# creates connections between different tables
from sqlalchemy.orm import relationship

# to get the current time
from sqlalchemy.sql import func

from db.database import Base

# meta information about the story
class Story(Base):

    # table name in the database
    __tablename__ = 'stories'

    # primary key for the story, as id is unique for each story(main identifier)
    #index means that this column will be indexed for faster queries
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    session_id = Column(String, index=True)

    #func.now() is used to set the default value of created_at to the current time
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # creates a connection to story node objects
    # back_populates is used to create a bidirectional relationship
    # between Story and StoryNode
    nodes = relationship("StoryNode", back_populates="story")

class StoryNode(Base):
    __tablename__ = 'story_nodes'

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey('stories.id'))  # Links to Story
    content = Column(String)
    is_root= Column(Boolean, default=False)  # Indicates if this is the root node  
    is_ending = Column(Boolean, default=False)  # Indicates if this is an ending node
    is_winning = Column(Boolean, default=False)  # Indicates if this is a winning node
    option= Column(JSON, default=list)  # Options for the node, if any
    
    # back reference to the story
    story = relationship("Story", back_populates="nodes")  # Back reference
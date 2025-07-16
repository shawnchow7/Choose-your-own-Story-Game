# creates a connection to the database
from sqlalchemy import create_engine

# to have a conversation with the database
from sqlalchemy.orm import sessionmaker

# provies a base class for all models
from sqlalchemy.ext.declarative import declarative_base


from core.config import setting

# creates a connection to your databse using the url from .env file
engine = create_engine(
    setting.DATABASE_URL
)

# to bind this engine to a session
# this session will be used to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#creates a base class for all models that will inherit from
Base=declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# creates database tables based on the models defined
def create_tables():

    # create all tables in the database
    Base.metadata.create_all(bind=engine)
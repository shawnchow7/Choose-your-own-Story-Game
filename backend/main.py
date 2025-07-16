from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import setting
from routers import story, job
from db.database import create_tables

# Create the database tables if they don't exist
create_tables()


# variable name of your FastAPI instance
app = FastAPI(
    title='Choose Your Own Adventure Game',
    description='api to generate cool game',
    version='0.1.0',
    docs_url='/docs',
    redoc_url='/redoc',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=setting.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

# include the routers for story and job
# this will allow you to access the endpoints defined in these routers
app.include_router(story.router, prefix=setting.API_PREFIX)
app.include_router(job.router, prefix=setting.API_PREFIX)

# in python every file has a special built-in variable called __name__
# when you run python main.py => __name__ get sets to __main__
if __name__ == "__main__":

    #web server to run our fast api
    import uvicorn

    #uvicorn needs to know where to find the fastapi instance which is the variable app
    uvicorn.run("main:app",host="0.0.0.0", port=8000, reload=True)
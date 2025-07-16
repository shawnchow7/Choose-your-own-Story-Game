#is for managing environment variables in a type-safe way

from typing import List

#class that read .env file automatically!!!!
from pydantic_settings import BaseSettings

# for custom validation logic
from pydantic import field_validator

# creates a class that inherits from BaseSettings
# This automatically reads environment variables and converts them to Python objects
class Setting(BaseSettings):
    # to specify all the environment variables in our .env file and what it type shoudl be
    API_PREFIX: str = '/api'

    DEBUG: bool = False

    DATABASE_URL: str

    ALLOWED_ORIGINS: str = ''

    OPEN_AI_KEY: str

    # for allowed origins dont just keep it as text, split it by comma then turn into list
    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return v.split(",") if v else []
    
    # belongs to the BaseSettings
    class Config:
        # read from .env file
        env_file= '.env'
        env_file_encoding = 'utf-8'
        case_sensitive=True

# creates an instance of the setting class
# when it actually starts to read the .env file and load all value
setting = Setting()
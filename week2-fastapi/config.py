import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    APP_NAME = os.getenv("APP_NAME")
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    PORT = os.getenv("PORT")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
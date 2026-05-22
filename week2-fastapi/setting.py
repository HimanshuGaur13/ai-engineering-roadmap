import os

from dotenv import load_dotenv

load_dotenv()


class Setting:

    APP_NAME = os.getenv("APP_NAME")
    ENVIRONMENT = os.getenv("ENVIRONMENT")
    PORT = os.getenv("PORT")
from dotenv import load_dotenv
import os

load_dotenv()

class Settings :
    API_HOST = os.getenv("API_HOST")

    API_PORT = os.getenv("API_PORT")

    MODEL_PATH = os.getenv("MODEL_PATH")

    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()
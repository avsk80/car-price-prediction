# loads env variables from a .env file and provides configuration settings for the application
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "CAR PRICE PREDICTION API"
    PROJECT_VERSION: str = "1.0.0"
    API_SECRET_KEY: str = os.getenv("API_KEY")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REDIS_URL: str = os.getenv("REDIS_URL")
    MODEL_PATH: str = "app/models/model.pkl"

settings = Settings()
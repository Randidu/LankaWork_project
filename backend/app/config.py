import os
from dotenv import load_dotenv
from urllib.parse import quote_plus


load_dotenv()

class Settings:
    PROJECT_NAME: str = "LankaWork Project"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Backend API for LankaWork system"


    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "Rana@2006")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_NAME: str = os.getenv("DB_NAME", "lankawork")

  
    SQLALCHEMY_DATABASE_URL: str = (
        f"mysql+pymysql://{DB_USER}:{quote_plus(DB_PASSWORD)}@{DB_HOST}/{DB_NAME}"
    )


    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()
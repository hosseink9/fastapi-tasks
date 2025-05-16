import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    database_host: str = os.getenv("DATABASE_HOST")
    database_port: str = os.getenv("DATABASE_PORT")
    database_name: str = os.getenv("DATABASE_NAME")
    database_user: str = os.getenv("DATABASE_USER")
    database_password: str = os.getenv("DATABASE_PASSWORD")

    @property
    def database_url(self):
        return (
            f"postgresql+asyncpg://{self.database_user}:{self.database_password}"
            f"@{self.database_host}:{self.database_port}/{self.database_name}"
        )

settings = Settings()

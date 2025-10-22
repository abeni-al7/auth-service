import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    ENVIRONMENT: str = "dev"
    APP_NAME: str = "Auth service"
    PORT: int
    DEBUG: bool = False
    DATABASE_URI: str
    JWT_SECRET_KEY: str
    JWT_EXPIRY_SECONDS: int

    model_config = SettingsConfigDict(
        env_file=f".env.{os.getenv("ENVIRONMENT", "dev")}",
        env_file_encoding="utf-8"
    )


settings = Settings()

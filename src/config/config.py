import os
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Manages application configuration settings.

    Loads settings from environment variables and an environment-specific
    .env file
    (e.g., .env.dev) determined by the `ENVIRONMENT` variable.
    """
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


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached instance of the application settings.
    """
    return settings

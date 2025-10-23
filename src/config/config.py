import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Manages application configuration settings.

    Loads settings from environment variables and an environment-specific
    .env file
    (e.g., .env.dev) determined by the `ENVIRONMENT` variable.
    """
    APP_NAME: str = "Auth service"
    PORT: int = Field(ge=1, le=65535)
    DEBUG: bool = False
    DATABASE_URI: str
    JWT_SECRET: str = Field(min_length=32)
    JWT_EXPIRY_SECONDS: int = Field(gt=0)

    model_config = SettingsConfigDict(
        env_file=f".env.{os.getenv("ENVIRONMENT", "dev")}",
        env_file_encoding="utf-8"
    )


_settings: Settings | None = None


def get_settings() -> Settings:
    """
     Return a cached instance of the application settings.
     """
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings

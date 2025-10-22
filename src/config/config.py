from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Auth service"
    PORT: int
    DEBUG: bool = False
    DATABASE_URI: str
    JWT_SECRET_KEY: str
    JWT_EXPIRY_SECONDS: int

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8")


settings = Settings()

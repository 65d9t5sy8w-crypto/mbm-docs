from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = "development"
    database_url: str = "postgresql+psycopg://mbm:mbm@localhost:5432/mbm"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="MBM_",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

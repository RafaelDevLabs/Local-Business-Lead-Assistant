from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = Field(
        default="Local Business Lead Assistant",
        validation_alias="PROJECT_NAME",
    )
    database_url: str = Field(
        default="postgresql+psycopg://postgres:postgres@localhost:5432/local_business_leads",
        validation_alias="DATABASE_URL",
    )
    llm_base_url: str = Field(
        default="http://127.0.0.1:1234/v1",
        validation_alias="LLM_BASE_URL",
    )
    llm_model: str = Field(
        default="qwen/qwen3-coder-30b",
        validation_alias="LLM_MODEL",
    )
    llm_api_key: str = Field(default="not-needed", validation_alias="LLM_API_KEY")
    business_notification_email: str | None = Field(
        default=None,
        validation_alias="BUSINESS_NOTIFICATION_EMAIL",
    )
    email_from: str | None = Field(
        default=None,
        validation_alias="EMAIL_FROM",
    )
    resend_api_key: str | None = Field(default=None, validation_alias="RESEND_API_KEY")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

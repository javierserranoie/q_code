from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from q_code_game.models import QCodeLanguage


class GameSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="QCODE_",
        case_sensitive=False,
    )

    web: str = Field(default="https://www.ure.es/codigo-q/")
    language: str = "short"
    max_attempts: int = Field(default=1, ge=1, le=3)
    difficulty: float = Field(default=1.0, ge=0.1, le=1.0)

    @field_validator("language")
    def validate_language(cls, v):
        if v not in QCodeLanguage.model_fields:
            raise ValueError(f"`language` must be one of {QCodeLanguage.model_fields}")
        return v

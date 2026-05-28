from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "PDF Analyser"

    database_url: str = "sqlite:///./pdfanalyser.db"

    gemini_api_key: str | None=None

    # upload_dir: str = "app/uploads"
    upload_dir: str = "storage/uploads"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()
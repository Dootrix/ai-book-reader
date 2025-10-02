from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "AI Book Reader API"
    database_url: str = "sqlite:///./app.db"


settings = Settings()

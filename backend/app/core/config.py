#config.py dosyası - uygulama ayarları 

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Last Light API"
    VERSION: str = "0.1.0"
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()
        
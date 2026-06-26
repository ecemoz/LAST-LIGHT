from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base
from app.models.user import User 


Base.metadata.create_all(bind=engine)  # Tabloları oluşturmak için

app = FastAPI(
   title = settings.PROJECT_NAME,
    version = settings.VERSION,
)


@app.get("/")
def root():
    return {"message": "Last Light API is running!"}


@app.get("/health") # sunucunun çalışıp çalışmadığını kontrol etmek için
def health_check():
    return {"status": "ok"}
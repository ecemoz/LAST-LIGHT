from fastapi import FastAPI
from app.core.config import settings

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
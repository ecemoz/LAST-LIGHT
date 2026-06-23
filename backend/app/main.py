from fastapi import FastAPI

app = FastAPI(
    title="Last Light API",
    description="Backend API for Last Light memory platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "Last Light API is running!"}


@app.get("/health") # sunucunun çalışıp çalışmadığını kontrol etmek için
def health_check():
    return {"status": "ok"}
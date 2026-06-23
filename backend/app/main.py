from fastapi import FastAPI


app = FastAPI(title="Last Light API")


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Last Light API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

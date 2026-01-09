from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Application is running"}

@app.get("/health")
def health():
    return {"health": "ok"}


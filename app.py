from fastapi import FastAPI

app = FastAPI(port=8080)

@app.get("/")
def index():
    return {"message": "Hello, World!"}
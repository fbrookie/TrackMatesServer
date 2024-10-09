# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/api/toy")
def get_toy():
    return {"message": "Hello from Google App Engine using Python 3.12!"}

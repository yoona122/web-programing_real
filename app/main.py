from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"massage:": "Hello Root!"}

@app.get("/home")
def home():
    return {"massage:": "Home!"}
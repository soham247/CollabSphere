from fastapi import FastAPI

app = FastAPI(title="CollabSphere")

@app.get("/")
def read_root():
    return {"message": "Welcome to CollabSphere"}
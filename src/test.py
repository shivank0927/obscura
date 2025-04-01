from fastapi import FastAPI

app = FastAPI()


@app.get("/")

def rever():
    
    return {"name": "shivank"}
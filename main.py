from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Credentials(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: Credentials):
    return {
        "username": data.username,
        "password": data.password
    }

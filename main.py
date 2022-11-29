from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_credentials = { "username": "", "password": "" }

class Credentials(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: Credentials):

    user_credentials["username"] = data.username
    user_credentials["password"] = data.password

    print("Saved credentials in cache:")
    print(user_credentials)

    return { "success": True }
    
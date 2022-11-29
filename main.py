from fastapi import FastAPI
from pydantic import BaseModel
from instagrapi import Client

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

@app.post("/upload_reel")
def upload_reel():

    client = Client()
    client.login(user_credentials["username"], user_credentials["password"])

    try:
        client.clip_upload("./reel.mp4", "Sample reel upload")
        return { "success": True }

    except Exception as e:
        print(f"Failed: {e}")
        return { "success": False }

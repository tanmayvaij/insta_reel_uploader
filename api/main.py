from fastapi import FastAPI
from pydantic import BaseModel
from instagrapi import Client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload_reel")
def upload_reel():

    client = Client()
    
    try:
        client.login("tony_bot_224", "tejomay123")
        client.clip_upload("./reel.mp4", "Sample reel upload")
        return { "success": True }

    except Exception as e:
        print(f"Failed: {e}")
        return { "success": False }

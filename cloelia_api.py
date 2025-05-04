# cloelia_api.py

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()  # read your .env

CLOELIA_KEY = os.getenv("CLOELIA_API_KEY")

app = FastAPI()

class EmotionRequest(BaseModel):
    emotion: str

@app.get("/")
async def root():
    return {"message": "Cloelia FastAPI is running!"}

@app.post("/analyze-emotion")
async def analyze_emotion(
    payload: EmotionRequest,
    authorization: str = Header(None)
):
    # check Bearer token
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing auth header")
    token = authorization.split(" ", 1)[1]
    if token != CLOELIA_KEY:
        raise HTTPException(401, "Invalid API key")

    # TODO: plug in your real emotion‐analysis logic here
    return {
        "emotion": payload.emotion,
        "analysis": f"Received and processed: {payload.emotion}"
    }


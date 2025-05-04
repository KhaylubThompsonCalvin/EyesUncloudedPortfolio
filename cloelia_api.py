# cloelia_api.py
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()        # so EnvVars from .env get picked up

class EmotionRequest(BaseModel):
    emotion: str

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Cloelia is alive at the root route!"}

@app.post("/analyze-emotion")
def analyze_emotion(
    payload: EmotionRequest,
    authorization: str = Header(None)
):
    # verify header
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, "Missing or invalid Authorization header")
    api_key = authorization.split(" ", 1)[1]
    if api_key != os.getenv("CLOELIA_API_KEY"):
        raise HTTPException(403, "Bad API key")

    # TODO: call OpenAI / ElevenLabs here
    return {
        "emotion_received": payload.emotion,
        "analysis": f"🔍 (pretend we ran AI on “{payload.emotion}”)"
    }

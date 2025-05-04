from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

class EmotionRequest(BaseModel):
    emotion: str

@app.get("/")
def read_root():
    return {"message": "Cloelia is alive at the root route!"}

@app.post("/analyze-emotion")
def analyze_emotion(
    payload: EmotionRequest,
    authorization: str = Header(None)
):
    # check Bearer token
    token = authorization.replace("Bearer ", "") if authorization else ""
    if token != os.getenv("CLOELIA_API_KEY"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {
        "emotion": payload.emotion,
        "analysis": f"You seem {payload.emotion}!"
    }

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
@app.get('/healthz')
def healthz():
    return {'status':'ok'}
@app.get('/healthz')
def healthz():
    return {'status':'ok'}

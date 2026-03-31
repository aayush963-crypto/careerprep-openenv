from fastapi import FastAPI
from pydantic import BaseModel
from env import CareerPrepEnv

app = FastAPI()
env = CareerPrepEnv()

class ResponseRequest(BaseModel):
    response: str

@app.post("/reset")
def reset():
    question = env.reset()
    return {
        "question": question
    }

@app.post("/step")
def step(req: ResponseRequest):
    reward, done, info = env.step(req.response)
    return {
        "reward": reward,
        "done": done,
        "info": info
    }

@app.get("/")
def root():
    return {"status": "CareerPrep OpenEnv server is running"}

from fastapi import FastAPI
from pydantic import BaseModel
from env import CareerPrepEnv

app = FastAPI(title="CareerPrep OpenEnv")

env = CareerPrepEnv()
current_question = None


class StepRequest(BaseModel):
    response: str


@app.get("/")
def home():
    return {
        "message": "CareerPrep OpenEnv is running",
        "endpoints": ["/reset", "/step", "/state"]
    }


@app.post("/reset")
def reset():
    global current_question
    current_question = env.reset()
    return {
        "observation": current_question,
        "done": False,
        "info": {
            "message": "Environment reset successful"
        }
    }


@app.post("/step")
def step(data: StepRequest):
    global current_question
    reward, done, info = env.step(data.response)
    current_question = None if done else info["next_question"]

    return {
        "reward": reward,
        "done": done,
        "observation": current_question,
        "info": info
    }


@app.get("/state")
def state():
    task_index = env.current_task_index
    done = task_index >= len(env.tasks)

    return {
        "current_task_index": task_index,
        "done": done,
        "current_observation": None if done else env.tasks[task_index]["question"]
    }
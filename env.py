from tasks import TASKS
from grader import grade_response

class CareerPrepEnv:
    def __init__(self):
        self.tasks = TASKS
        self.current_task_index = 0

    def reset(self):
        self.current_task_index = 0
        return self.tasks[self.current_task_index]["question"]

    def get_current_task(self):
        return self.tasks[self.current_task_index]

    def step(self, response: str):
        task = self.tasks[self.current_task_index]
        reward = grade_response(response, task["expected_keywords"])

        self.current_task_index += 1
        done = self.current_task_index >= len(self.tasks)

        next_question = None if done else self.tasks[self.current_task_index]["question"]

        info = {
            "task_id": task["id"],
            "reward": reward,
            "next_question": next_question
        }

        return reward, done, info
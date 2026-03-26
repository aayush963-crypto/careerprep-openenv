from env import CareerPrepEnv
from baseline_agent import simple_agent

env = CareerPrepEnv()
question = env.reset()

total_reward = 0
task_count = 0

while True:
    print("\nTask:", question)

    response = simple_agent(question)
    print("Agent Response:", response)

    reward, done, info = env.step(response)

    print("Reward:", reward)
    print("Info:", info)

    total_reward += reward
    task_count += 1

    if done:
        break

    question = info["next_question"]

average_score = total_reward / task_count
print("\nFinal Average Score:", round(average_score, 2))
from stable_baselines3 import PPO
from acc_env import CustomACCEnv

# Load the trained model
model = PPO.load("ppo_acc_model_final.zip")
env = CustomACCEnv()

episodes = 100
for ep in range(episodes):
    obs, _ = env.reset()
    done = False
    total_reward = 0
    while not done:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, _, _ = env.step(action)
        total_reward += reward
    print(f"Episode {ep + 1}: Total Reward = {total_reward}")

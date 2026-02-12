import torch
from stable_baselines3 import PPO

model = PPO.load("ppo_acc_model_final.zip")
policy = model.policy

dummy_input = torch.randn(1, model.observation_space.shape[0])
torch.onnx.export(policy, dummy_input, "ppo_policy.onnx", opset_version=11)

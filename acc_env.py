import gymnasium as gym
import numpy as np
from gymnasium import spaces

class CustomACCEnv(gym.Env):
    def __init__(self):
        super(CustomACCEnv, self).__init__()

        # Observation space: 3-dimensional (matches dummy_input (1,3))
        self.observation_space = spaces.Box(
            low=-np.inf,
            high=np.inf,
            shape=(3,),
            dtype=np.float32
        )

        # Action space: 4 discrete actions (matches Dense(4))
        self.action_space = spaces.Discrete(4)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        state = np.zeros(3, dtype=np.float32)
        return state, {}

    def step(self, action):
        next_state = np.zeros(3, dtype=np.float32)
        reward = 0.0
        terminated = True
        truncated = False
        info = {}

        return next_state, reward, terminated, truncated, info

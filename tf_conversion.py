import tensorflow as tf
import numpy as np

# Define TensorFlow PPO policy architecture
class PPOPolicyTF(tf.keras.Model):
    def __init__(self):
        super(PPOPolicyTF, self).__init__()
        self.dense1 = tf.keras.layers.Dense(64, activation='relu')
        self.dense2 = tf.keras.layers.Dense(64, activation='relu')
        self.logits = tf.keras.layers.Dense(4)  # Adjust number of actions here

    def call(self, x):
        x = self.dense1(x)
        x = self.dense2(x)
        return self.logits(x)

# Instantiate model
tf_policy = PPOPolicyTF()

# Build model by running dummy input through it
dummy_input = tf.random.uniform((1, 3))  # Batch size 1, input dim 3
_ = tf_policy(dummy_input)

# Load PyTorch weights saved as numpy arrays
weights = np.load("ppo_weights.npz")

# Assign PyTorch weights to TensorFlow model (transpose matrices)
tf_policy.dense1.weights[0].assign(weights['mlp_extractor.policy_net.0.weight'].T)
tf_policy.dense1.weights[1].assign(weights['mlp_extractor.policy_net.0.bias'])
tf_policy.dense2.weights[0].assign(weights['mlp_extractor.policy_net.2.weight'].T)
tf_policy.dense2.weights[1].assign(weights['mlp_extractor.policy_net.2.bias'])
tf_policy.logits.weights[0].assign(weights['action_net.weight'].T)
tf_policy.logits.weights[1].assign(weights['action_net.bias'])

print("Weights loaded successfully!")

# Save the model as TensorFlow SavedModel if needed
tf_policy.save("ppo_tf_saved_model")
print("TensorFlow model saved as 'ppo_tf_saved_model'")

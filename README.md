# AI-Adaptive-Cruise-Control-with-Reinforcement-Learning

Reinforcement Learning–based Adaptive Cruise Control (ACC) pipeline including model evaluation, ONNX export, and TensorFlow policy reconstruction.

---

## Project Overview

This project demonstrates a Proximal Policy Optimization (PPO)–based Adaptive Cruise Control (ACC) framework designed for embedded deployment scenarios.

The repository includes:

* Policy evaluation pipeline
* PyTorch → ONNX export
* PyTorch → TensorFlow weight conversion
* Custom ACC environment definition

Pretrained artifacts are not included in this repository.

---

## Reinforcement Learning Model

* **Algorithm:** Proximal Policy Optimization (PPO)
* **Policy Type:** MLP Policy
* **Input Dimension:** 3
* **Action Space:** 4 discrete actions
* **Frameworks Used:** Stable-Baselines3, PyTorch, TensorFlow

The TensorFlow model replicates the PPO policy architecture using two hidden layers (64 units each) followed by a 4-output action layer.

---

## Model Conversion Pipeline

### Evaluation

Loads a trained PPO model and runs it for 100 episodes:

```bash
python evaluation.py
```

Requires:

* `ppo_acc_model_final.zip`

---

### ONNX Export

Exports the trained PyTorch policy to ONNX format:

```bash
python export_onnx.py
```

Output:

```
ppo_policy.onnx
```

Requires:

* `ppo_acc_model_final.zip`

---

### TensorFlow Conversion

Reconstructs the PPO policy architecture in TensorFlow and loads weights from a NumPy archive:

```bash
python tf_conversion.py
```

Output:

```
ppo_tf_saved_model/
```

Requires:

* `ppo_weights.npz`

---

## Custom Environment

`acc_env.py` defines a custom Gymnasium environment:

* Observation space: 3-dimensional
* Action space: 4 discrete actions

This environment is required for model evaluation.

---

## 📂 Repository Structure

```
.
├── tf_conversion.py
├── evaluation.py
├── export_onnx.py
├── acc_env.py
├── requirements.txt
├── docs/
│   ├── Problem_Statement.pdf
│   └── Report.pdf
└── images/
```

---

## Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

---

## Model Artifacts

The following files are not included:

* `ppo_acc_model_final.zip`
* `ppo_weights.npz`

These are required to run evaluation and conversion scripts.

---

##  Technical Scope

This repository focuses on:

* Reinforcement learning policy evaluation
* Cross-framework model portability (PyTorch → ONNX → TensorFlow)
* Structural alignment of policy architecture across frameworks
* Preparation for embedded deployment workflows

---
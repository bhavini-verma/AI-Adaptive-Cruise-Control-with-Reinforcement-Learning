# AI-Adaptive-Cruise-Control-with-Reinforcement-Learning

> Real-time embedded reinforcement learning deployment using TensorFlow Lite Micro under memory and power constraints.

---

## Project Objective

Design and deploy a low-latency Adaptive Cruise Control (ACC) system on a resource-constrained microcontroller (ESP32) capable of maintaining safe following distance using on-device reinforcement learning inference.

The system eliminates cloud dependency and executes the policy entirely on embedded hardware.

This repository also includes the reinforcement learning evaluation and cross-framework model conversion pipeline used prior to embedded deployment.

---

## System Architecture

```
HC-SR04 Sensor
      ↓
Distance Acquisition
      ↓
State Normalization
      ↓
TensorFlow Lite Micro Inference (INT8 PPO Policy)
      ↓
Discrete Action Selection
      ↓
PWM Signal Generation
      ↓
L298N Motor Driver
      ↓
DC Motor Speed Adjustment
```

The control loop runs continuously, performing sensing → inference → actuation in real time.

---

## Reinforcement Learning Model

* **Algorithm:** Proximal Policy Optimization (PPO)
* **Policy Type:** MLP Policy
* **Deployment Format:** TensorFlow Lite Micro
* **Quantization:** INT8
* **Original Model Size:** 1.8 MB
* **Deployed Model Size:** 230 KB
* **Inference Latency:** ~25 ms (on ESP32)

The model outputs discrete throttle actions mapped to PWM duty cycles for motor control.

---

## Model Pipeline (Pre-Deployment)

This repository contains the RL processing pipeline used before embedded deployment:

### Evaluation

Runs trained PPO model for 100 episodes.

```
python evaluation.py
```

### ONNX Export

Exports PyTorch policy to ONNX format.

```
python export_onnx.py
```

### TensorFlow Reconstruction

Rebuilds PPO architecture in TensorFlow and loads saved weights.

```
python tf_conversion.py
```

---

## Hardware Components

| Component                 | Role                                   |
| ------------------------- | -------------------------------------- |
| ESP32 DevKit              | Edge inference + control logic         |
| HC-SR04 Ultrasonic Sensor | Distance measurement (10–100 cm range) |
| L298N Motor Driver        | PWM-based motor actuation              |
| DC Motor                  | Vehicle velocity simulation            |

---

## Embedded Implementation

* Firmware written in **C++**
* Tensor arena allocated statically for TFLite Micro
* Continuous polling-based control loop
* Distance normalization before inference
* Discrete action → PWM mapping logic
* No external accelerator or cloud compute

The system operates within microcontroller memory constraints while maintaining stable control behavior.

---

## Performance Metrics

| Metric                    | Value  |
| ------------------------- | ------ |
| Decision Accuracy         | 94.3%  |
| Dynamic Stability         | 96.2%  |
| Overall System Efficiency | 95.4%  |
| Inference Latency         | ~25 ms |
| Runtime Power Consumption | ~2.8 W |

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

## Model Artifacts

Pretrained model files are not included:

* `ppo_acc_model_final.zip`
* `ppo_weights.npz`

These are required to execute evaluation and conversion scripts.

---
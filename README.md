# Emotionally-Aware Autonomous Vehicle and Robotics using EBPL

## 📌 Project Overview

This project simulates an **Emotionally-Aware Autonomous Vehicle and Robotics System** using **Experience-Based Progressive Learning (EBPL)**. It demonstrates intelligent, adaptive behavior in navigation and obstacle avoidance, mimicking human-like emotional decision-making.

Developed as part of the **Naan Mudhalvan Phase Project**, this system integrates pathfinding, emotion-driven logic, and visual simulation — all in a lightweight software environment using Python.

---

## 🎯 Objective

To build a simulated autonomous vehicle that:
- Makes intelligent decisions using EBPL (Experience-Based Progressive Learning)
- Adapts emotionally based on previous outcomes
- Avoids obstacles and visualizes decisions clearly

---

## 🧠 Problem Statement

Traditional autonomous vehicles rely heavily on rule-based logic and struggle to adapt to complex or dynamic environments. This project solves that by:
- Using emotion modeling for adaptive driving behavior
- Logging past experiences to improve future decisions
- Enabling real-time simulation with minimal hardware

---

## 🛠️ Technology Stack

- **Python** – Core logic and simulation
- **OpenCV** – (optional for camera vision)
- **Matplotlib** – Data visualization
- **JSON** – Log/Experience storage (conceptualized)
- **Flask** – (Future scope: dashboard interface)

---

## 🔑 Key Features

- ✅ Emotion-based behavior simulation (defensive, aggressive)
- ✅ Obstacle detection using position logic and A* pathfinding
- ✅ Visual plots for car, destination, path, and obstacles
- ✅ Experience-based logic using EBPL simulation
- ✅ Real-time random and predefined test scenarios

---

## 🧪 How It Works

### 1. **Emotion Simulation & Path Drawing**
- Car starts at `(1, 1)` and aims for destination `(9, 9)`
- A random obstacle is generated in the grid
- If the obstacle lies on the direct path:
  - The path is drawn in **red** (emotionally defensive)
  - Otherwise, drawn in **green** (safe)

### 2. **A* Algorithm for Smart Navigation**
- Grid-based environment with fixed obstacles
- Uses **A* Search Algorithm** to find the shortest path
- Path is plotted avoiding obstacles with a **green line**
- All steps printed in terminal for clarity

---

## 📂 Files Included

| File Name           | Description                                  |
|---------------------|----------------------------------------------|
| `program.py`        | Combined simulation script with both models  |
| `Dataset.pdf`       | Project concept, report, or test data        |
| `output.png`        | Screenshot of visual output                  |
| `README.md`         | Project documentation                        |

---
## 📊 Dataset Description

The dataset comprises 160 entries, each representing a unique driving scenario with the following attributes:

- **Sensor Temperature (°C)**: Simulated temperature readings from the vehicle's sensors.
- **Response Time (s)**: Time taken by the vehicle to respond to a specific event.
- **Scenario**: Describes the driving situation (e.g., "Obstacle Detected", "Pedestrian Nearby").
- **Vehicle Mood**: The emotional state of the vehicle (e.g., "Defensive", "Aggressive").

---

## 🔮 Future Scope

- Add real-time camera integration using OpenCV
- Build a Flask dashboard for live monitoring
- Extend to real-world robotic prototype with sensors
- Introduce multi-agent coordination and emotion-based decision switching# Autonomous-Vehicles-and-Robotics

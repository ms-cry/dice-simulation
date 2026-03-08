# Dice Probability Simulation 🎲

This project simulates **10,000 dice rolls** using Python and compares the **experimental probability** with the **theoretical probability** of a fair dice.

The goal is to demonstrate the **Law of Large Numbers**, which states that as the number of trials increases, the experimental probability approaches the theoretical probability.

---

## 📊 Concepts Used

* NumPy arrays
* Random number simulation
* Probability basics
* Data visualization using Matplotlib
* Law of Large Numbers

---

## ⚙️ How It Works

1. A fair dice is simulated **10,000 times** using NumPy.
2. The number of occurrences of each dice face (1–6) is counted.
3. Experimental probabilities are calculated.
4. A bar chart is plotted to compare experimental probabilities with the theoretical probability.

The theoretical probability for each face of a fair dice is:

P(face) = 1 / 6 ≈ **0.1667**

---

## 📈 Output

The program generates a bar chart showing:

* Experimental probability of each dice face
* A red horizontal line representing the theoretical probability (1/6)

This visually demonstrates how experimental results converge toward theoretical values.

---

## 🧪 Example Output

Counts:
[1680 1662 1703 1648 1645 1662]

Probabilities:
[0.168 0.166 0.170 0.165 0.164 0.166]

---

## ▶️ How to Run

### 1️⃣ Clone the repository

git clone https://github.com/ms-cry/dice-simulation.git

cd dice-probability-simulation

### 2️⃣ Install dependencies

pip install -r requirements.txt

### 3️⃣ Run the script

python dice_simulation.py

---

## 📂 Project Structure

dice-probability-simulation

│
├── dice_simulation.py
├── README.md
└── requirements.txt

---

## 📚 Learning Outcome

This project helps beginners understand:

* Probability through simulation
* NumPy random number generation
* Basic data visualization
* Statistical intuition

---
# dice-simulation

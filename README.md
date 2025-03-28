# Gambler's Ruin Simulation Project

This project simulates the classic **Gambler's Ruin** problem using Python.

The simulation is implemented in 3 steps:

### 🧩 Problem 1 – `simulation.py`
A basic simulation of the gambler’s ruin problem where:
- The game is fair (p = 0.5)
- The gambler bets $1 per round
- The goal is to reach a certain amount or go broke

### 🔁 Problem 2 – `general_simulation.py`
This generalizes the problem with user-defined parameters:
- Win probability `p`
- Payout multiplier `q`
- Bet size `j`
- Starting money `i`
- Goal amount `n`

### 💰 Problem 3 – `realistic_simulation.py`
A more realistic version with:
- Credit line
- Adaptive betting (Martingale)
- Maximum table bet

---

### 💻 Run the App with UI
We used **Streamlit** for a user interface.

To launch it:

```bash
streamlit run ui.py

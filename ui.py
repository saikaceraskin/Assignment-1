import streamlit as st
import requests

st.set_page_config(page_title="Gambler's Ruin Simulator", layout="centered")

st.title("🎲 Gambler's Ruin Simulator")
st.markdown("Adjust the parameters and run the simulation!")

# Input sliders and boxes
p = st.slider("Probability of Winning (p)", 0.01, 0.99, 0.5, 0.01)
q = st.number_input("Payout Multiplier (q)", value=2.0)
bet = st.number_input("Bet Size", value=1.0)
start = st.number_input("Starting Money", value=10.0)
goal = st.number_input("Goal Money", value=20.0)
credit = st.number_input("Credit Limit", value=10.0)
max_bet = st.number_input("Max Bet Allowed", value=16.0)
trials = st.number_input("Number of Simulations", value=10000, step=1000)

# Button to call the API
if st.button("Run Simulation"):
    with st.spinner("Simulating..."):
        try:
            url = "http://127.0.0.1:5050/simulate"
            params = {
                "p": p,
                "q": q,
                "bet": bet,
                "start": start,
                "goal": goal,
                "credit": credit,
                "max": max_bet,
                "trials": trials
            }
            response = requests.get(url, params=params)
            data = response.json()

            if "error" in data:
                st.error(f"Error: {data['error']}")
            else:
                st.success("Simulation Complete!")
                st.metric("🟢 Probability of Winning", f"{data['win_probability'] * 100:.2f}%")
                st.metric("🔴 Probability of Going Broke", f"{data['loss_probability'] * 100:.2f}%")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

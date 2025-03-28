from flask import Flask, request, jsonify
from realistic_simulation import realistic_gambler_simulation

app = Flask(__name__)

@app.route("/simulate", methods=["GET"])
def simulate():
    try:
        # Get parameters from the query string
        p = float(request.args.get("p", 0.5))
        q = float(request.args.get("q", 2))
        bet_size = float(request.args.get("bet", 1))
        start_amount = float(request.args.get("start", 10))
        goal_amount = float(request.args.get("goal", 20))
        credit_limit = float(request.args.get("credit", 10))
        max_bet = float(request.args.get("max", 16))
        trials = int(request.args.get("trials", 10000))

        win, lose = realistic_gambler_simulation(
            p, q, bet_size, start_amount, goal_amount, credit_limit, max_bet, trials
        )

        return jsonify({
            "win_probability": round(win, 3),
            "loss_probability": round(lose, 3)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5050)

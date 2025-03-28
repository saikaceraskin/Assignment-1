import random

def realistic_gambler_simulation(p, q, bet_size, start_amount, goal_amount,
                                  credit_limit, max_bet, trials=10000):
    """
    Simulates a more realistic gambler's ruin scenario with:
    - a line of credit (can go negative up to credit_limit)
    - adaptive betting based on losing streak
    - a max bet per table

    Parameters:
    - p: probability of winning
    - q: payout multiplier
    - bet_size: base bet size
    - start_amount: starting money
    - goal_amount: target money
    - credit_limit: maximum amount gambler can borrow (e.g., 10 means money can go down to -10)
    - max_bet: maximum allowed bet at the table
    - trials: number of simulation runs

    Returns:
    - win_probability: how often the gambler reached the goal
    - loss_probability: how often the gambler went bankrupt
    """
    win_count = 0

    for _ in range(trials):
        money = start_amount
        streak = 0  # losing streak

        while credit_limit * -1 < money < goal_amount:
            # Calculate adaptive bet based on losing streak
            current_bet = bet_size * (1 / p) ** streak
            current_bet = min(current_bet, max_bet)  # apply table max

            if money < current_bet:
                break  # can't place the bet, considered broke

            if random.random() < p:
                gain = current_bet * (q - 1)
                money += gain
                streak = 0  # reset streak on win
            else:
                money -= current_bet
                streak += 1  # losing streak increases

        if money >= goal_amount:
            win_count += 1

    win_probability = win_count / trials
    loss_probability = 1 - win_probability
    return win_probability, loss_probability


# Example usage
if __name__ == "__main__":
    p = 0.5
    q = 2
    bet_size = 1
    start_amount = 10
    goal_amount = 20
    credit_limit = 10
    max_bet = 16

    win, lose = realistic_gambler_simulation(
        p, q, bet_size, start_amount, goal_amount, credit_limit, max_bet
    )

    print(f"Probability of winning: {win:.3f}")
    print(f"Probability of going broke: {lose:.3f}")

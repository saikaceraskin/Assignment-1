import random

def generalized_gambler_simulation(p, q, bet_size, start_amount, goal_amount, trials=10000):
    """
    Simulates the generalized gambler's ruin problem.

    Parameters:
    - p: probability of winning a single game (0 < p < 1)
    - q: payout multiplier if the gambler wins (e.g. 2 for double)
    - bet_size: the amount bet each round
    - start_amount: initial amount of money
    - goal_amount: target amount of money
    - trials: number of simulations to run

    Returns:
    - win_probability: probability of reaching the goal
    - loss_probability: probability of going broke
    """
    win_count = 0

    for _ in range(trials):
        money = start_amount
        while 0 < money < goal_amount:
            if money < bet_size:
                break  # not enough to place a bet
            if random.random() < p:
                money += bet_size * (q - 1)  # gain
            else:
                money -= bet_size  # loss
        if money >= goal_amount:
            win_count += 1

    win_probability = win_count / trials
    loss_probability = 1 - win_probability
    return win_probability, loss_probability


# Example usage
if __name__ == "__main__":
    p = 0.5             # 50% chance of winning
    q = 2               # payout is 2x on win
    bet_size = 1        # bet size is $1
    start_amount = 10   # starting with $10
    goal_amount = 20    # goal is $20

    win, lose = generalized_gambler_simulation(p, q, bet_size, start_amount, goal_amount)
    print(f"Probability of winning: {win:.3f}")
    print(f"Probability of going broke: {lose:.3f}")

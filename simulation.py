import random

def gambler_ruin_simulation(start_money, goal_money, trials=10000):
    win_count = 0

    for _ in range(trials):
        money = start_money
        while 0 < money < goal_money:
            if random.random() < 0.5:
                money += 1
            else:
                money -= 1
        if money == goal_money:
            win_count += 1

    win_prob = win_count / trials
    lose_prob = 1 - win_prob
    return win_prob, lose_prob


# Örnek kullanım
if __name__ == "__main__":
    win, lose = gambler_ruin_simulation(start_money=10, goal_money=20)
    print(f"Kazanma olasılığı: {win:.3f}")
    print(f"Batma olasılığı: {lose:.3f}")

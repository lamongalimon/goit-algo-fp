
def greedy_algorithm(items, budget):
    chosen = []
    total_calories = 0
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    for name, data in sorted_items:
        if data['cost'] <= budget:
            budget -= data['cost']
            total_calories += data['calories']
            chosen.append(name)
    return chosen, total_calories





def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    chosen = [[] for _ in range(budget + 1)]
    for name, data in items.items():
        cost, cal = data["cost"], data["calories"]
        for b in range(budget, cost - 1, -1):
            if cal + dp[b - cost] > dp[b]:
                dp[b] = cal + dp[b - cost]
                chosen[b] = chosen[b - cost] + [name]
    return chosen[budget], dp[budget]


items = {
  "pizza": {"cost": 50, "calories": 300},
  "hamburger": {"cost": 40, "calories": 250},
  "hot-dog": {"cost": 30, "calories": 200},
  "pepsi": {"cost": 10, "calories": 100},
  "cola": {"cost": 15, "calories": 220},
  "potato": {"cost": 25, "calories": 350}
}


print("Greedy:", greedy_algorithm(items, 100))
print("DP:    ", dynamic_programming(items, 100))
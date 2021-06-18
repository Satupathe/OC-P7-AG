maximum_price = 500
action_list = [["action_01", 20, 5],
               ["action_02", 30, 10],
               ["action_03", 50, 15],
               ["action_04", 70, 20],
               ["action_05", 60, 17],
               ["action_06", 80, 25],
               ["action_07", 22, 7],
               ["action_08", 26, 11],
               ["action_09", 48, 13],
               ["action_10", 34, 27],
               ["action_11", 42, 17],
               ["action_12", 110, 9],
               ["action_13", 38, 23],
               ["action_14", 14, 1],
               ["action_15", 18, 3],
               ["action_16", 8, 8],
               ["action_17", 4, 12],
               ["action_18", 10, 14],
               ["action_19", 2, 21],
               ["action_20", 114, 18]
               ]

for action in action_list:
    price = action[1]
    profit = action[2]
    action[2] = int(round(price * (profit/100)))


def knapsack(capacity, actions):
    """
    Find for each action if it's worth or not to keep it 
    and add it's value to the total
    """
    investment = capacity
    number_of_actions = len(actions)
    keeping_table = [[[], 0, 0] for x in range(investment+1)]

    for n in range(1, number_of_actions+1, 1):
        actual_action = actions[n-1]
        name = actual_action[0]
        price = actual_action[1]
        profit = actual_action[2]

        for p in range(investment, price, -1):
            best_minus_price = keeping_table[p-price]
            best_with_actual_price = keeping_table[p]
            actual_profit = best_minus_price[2] + profit

            if actual_profit > best_with_actual_price[2]:
                keeping_table[p][0] = best_minus_price[0] + [name]
                keeping_table[p][1] = best_minus_price[1] + price
                keeping_table[p][2] = actual_profit
    return keeping_table[-1]


results = knapsack(maximum_price, action_list)

print(f"La meilleure combinaison d'achat est: {results[0]}")
print(f"Le prix d'achat total est de {results[1]} euros")
print(f"L'estimation de gain est de {results[2]} euros")

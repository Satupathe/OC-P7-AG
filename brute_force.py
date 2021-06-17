import itertools


action_table = {"action_01": [20, 5],
                "action_02": [30, 10],
                "action_03": [50, 15],
                "action_04": [70, 20],
                "action_05": [60, 17],
                "action_06": [80, 25],
                "action_07": [22, 7],
                "action_08": [26, 11],
                "action_09": [48, 13],
                "action_10": [34, 27],
                "action_11": [42, 17],
                "action_12": [110, 9],
                "action_13": [38, 23],
                "action_14": [14, 1],
                "action_15": [18, 3],
                "action_16": [8, 8],
                "action_17": [4, 12],
                "action_18": [10, 14],
                "action_19": [2, 21],
                "action_20": [114, 18]
                }

final_gains = 0
best_investment = []
for i in range(len(action_table) + 1):
    for element in (itertools.combinations(action_table, r=i)):
        sum = 0
        price_max = 500
        purchase_price = 0

        for action in element:
            price = action_table[action][0]
            gain_multiplier = (action_table[action][1])/100
            purchase_price += price
            sum += price * gain_multiplier
        if purchase_price <= price_max:
            if sum > final_gains:
                final_gains = sum
                best_investment = element
        else:
            pass

print(f"La meilleure combinaison d'achat est: {best_investment}")
print(f"L'estimation de gain est de {final_gains}")

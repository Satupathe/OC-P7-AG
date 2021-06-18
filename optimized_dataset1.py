import csv


maximum_price = 500
action_list = []


def get_csv():
    """get and clean actions infos for the csv file"""
    filename = 'dataset1_Python+P7.csv'
    with open(filename,
              mode='r',
              newline='',
              encoding="utf8",
              errors='ignore') as csvfile:
        infos = csv.reader(csvfile, quoting=csv.QUOTE_ALL, delimiter=',')
        for row in infos:
            one_action = []
            for element in row:
                if "Share" in element:
                    one_action.append(element)
                elif "name" in element:
                    one_action.append(element)
                elif "price" in element:
                    one_action.append(element)
                elif "profit" in element:
                    one_action.append(element)
                else:
                    number = float(element)
                    if number == 0:
                        one_action = []
                        break
                    elif number < 0:
                        number = abs(number)
                    one_action.append(number)
            if len(one_action) == 3:
                action_list.append(one_action)


get_csv()

action_list.remove(action_list[0])

for raw_action in action_list:
    if len(raw_action) != 3:
        action_list.remove(raw_action)

for corrected_action in action_list:
    price = corrected_action[1]
    profit = corrected_action[2]
    corrected_action[2] = int(round(price * profit))
    corrected_action[1] = int(corrected_action[1]*100)


def knapsack(capacity, actions):
    """
    Find for each action if it's worth or not to keep it 
    and add it's value to the total
    """
    investment = capacity * 100
    number_of_actions = len(actions)
    print(number_of_actions)
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
print(f"Le prix d'achat total est de {results[1]/100} euros")
print(f"L'estimation de gain est de {results[2]/100} euros")

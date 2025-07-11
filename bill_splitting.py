# This program reports how much individuals should pay for their order at
# dinner.
#
# Usage:
#
# $ python bill_splitting.py [name]
#
# For instance:
#
# $ python bill_splitting.py Tom
# Tom should pay 38.55
#
# or:
#
# $ python bill_splitting.py Tim
# Tim did not have dinner

import sys
import collections

BILL_ITEMS = [
    ["Tom", "Calamari", 6.00],
    ["Tom", "American Hot", 11.50],
    ["Tom", "Chocolate Fudge Cake", 4.45],
    ["Clare", "Bruschetta Originale", 5.35],
    ["Clare", "Fiorentina", 10.65],
    ["Clare", "Tiramasu", 4.90],
    ["Rich", "Bruschetta Originale", 5.35],
    ["Rich", "La Reine", 10.65],
    ["Rich", "Honeycomb Cream Slice", 4.90],
    ["Rosie", "Garlic Bread", 4.35],
    ["Rosie", "Veneziana", 9.40],
    ["Rosie", "Tiramasu", 4.90],
]


def main(name):
    if name is None:
        print_order_table()
    else:
        print_individual_bill_amount(name)
        print_order_breakdown()


def print_individual_bill_amount(name):

    if get_amounts_owed().get(name) is None:
        print(f"{name} did not have dinner")
        return

    print(f"{name} should pay {get_amounts_owed().get(name)}")


def print_order_breakdown():
    print("\nHere is a breakdown of what each person had to eat:")
    for person, order in get_dishes_and_prices().items():
        print(
            f"{person} ate the following dishes: {', '.join(dish for dish in order[1])}"
        )


def print_order_table():
    print(
        "\nHere is a breakdown of what each person had to eat and the amount they owe:\n"
    )
    print(
        f"{'Name':<11} | {'Starter':<20} | {'Main':<15} | {'Dessert':<22} | {'Amount owed (£)'}\n----------------------------------------------------------------------------------------------"
    )
    for person, orders in get_dishes_and_prices().items():
        print(
            f"{person:<11} | {orders[1][0]:<20} | {orders[1][1]:<15} | {orders[1][2]:<22} | {orders[0]}"
        )

def get_amounts_owed():
    amount_owed_dict = collections.defaultdict(float)
    for order in BILL_ITEMS:
        amount_owed_dict[order[0]] += order[2]

    return amount_owed_dict

def get_dishes_and_prices():
    orders_dict = get_amounts_owed()
    for person in orders_dict.keys():
        dishes = [order[1] for order in BILL_ITEMS if order[0] == person]
        orders_dict[person] = [orders_dict[person], dishes]

    return orders_dict

if __name__ == "__main__":
    if len(sys.argv) < 2:
        main(None)
    else:
        main(sys.argv[1])

# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that it additionally reports a breakdown of what each
#   person had to eat.
# * Change the program so that if it is called without arguments, a table of
#   how much everybody should pay is displayed

# TODO (extra-extra):
# * Use collections.defaultdict
# * Use sys.argv

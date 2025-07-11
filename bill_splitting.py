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
import itertools
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


def get_names_for_keys(bill_item):
    return bill_item[0]


ORDERS_BY_INDIVIDUAL = {
    key: [subgroup[1:] for subgroup in list(group)]
    for key, group in itertools.groupby(
        sorted(BILL_ITEMS, key=get_names_for_keys), key=get_names_for_keys
    )
}


def main(name):
    print(name)
    if name is None:
        print_order_table()
    else:
        print_individual_bill_amount(name)
        print_order_breakdown()


def print_individual_bill_amount(name):

    amount_owed = get_individual_amount_owed(name)

    if amount_owed is None:
        print(f"{name} did not have dinner")
        return

    print(f"{name} should pay {amount_owed}")


def print_order_breakdown():
    print("\nHere is a breakdown of what each person had to eat:")
    for person, order in ORDERS_BY_INDIVIDUAL.items():
        print(
            f"{person} ate the following dishes: {', '.join(dish[0] for dish in order)}"
        )


def print_order_table():
    print(
        "\nHere is a breakdown of what each person had to eat and the amount they owe:\n"
    )
    print(
        f"{'Name':<11} | {'Starter':<20} | {'Main':<15} | {'Dessert':<22} | {'Amount owed (£)'}\n----------------------------------------------------------------------------------------------"
    )
    for person, orders in ORDERS_BY_INDIVIDUAL.items():
        print(
            f"{person:<11} | {orders[0][0]:<20} | {orders[1][0]:<15} | {orders[2][0]:<22} | {sum(order[1] for order in orders)}"
        )

def get_individual_amount_owed(name):
    amount_owed_dict = collections.defaultdict(list)
    for order in BILL_ITEMS:
        amount_owed_dict[order[0]].append(order[2])

    if amount_owed_dict.get(name):
        return sum(amount_owed_dict.get(name))
    else:
        return None

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

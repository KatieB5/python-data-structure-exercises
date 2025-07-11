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

import argparse
import itertools

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


def main():
    name = get_args().get("name")
    if name is None:
        print_order_table()
    else:
        print_individual_bill_amount(name)
        print_order_breakdown()


def get_args():
    parser = argparse.ArgumentParser(
        prog="Bill Splitting",
        description="This program reports how much individuals should pay for their order at dinner",
    )

    parser.add_argument(
        "name",
        help="The name of the person whose total order amount you want",
        nargs="?",
        type=str,
    )

    return vars(parser.parse_args())


def print_individual_bill_amount(name):
    individual_orders = ORDERS_BY_INDIVIDUAL.get(name)

    if individual_orders is None:
        print(f"{name} did not have dinner")
        return

    total_amount_owed_by_individual = sum(order[1] for order in individual_orders)

    print_message(name, total_amount_owed_by_individual)


def print_message(name, total_amount_owed_by_individual):
    print(f"{name} should pay {total_amount_owed_by_individual}")


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


if __name__ == "__main__":
    main()

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

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

bill_items = [
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


def main():
    name = get_args()


def get_args():
    parser = argparse.ArgumentParser(
        prog="Bill Splitting",
        description="This program reports how much individuals should pay for their order at dinner",
    )

    parser.add_argument(
        "name",
        help="The name of the person who's total order amount you want",
        nargs="?",
        default="",
        type=str,
    )

    return vars(parser.parse_args())


if __name__ == "__main__":
    main()

# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that it additionally reports a breakdown of what each
#   person had to eat.
# * Change the program so that if it is called without arguments, a table of
#   how much everybody should pay is displayed

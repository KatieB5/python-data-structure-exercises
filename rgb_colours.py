# This program knows about the RGB code corresponding to common colours.
#
# Usage:
#
# $ python rgb_colours.py [colour]
#
# For instance:
#
# $ python rgb_colours.py red
# The RGB code for red is F00
#
# or:
#
# $ python rgb_colours.py "burnt sienna"
# I don't know the RGB code for burnt sienna

import argparse

colours = [
    ['red', 'F00'],
    ['yellow', 'FF0'],
    ['green', '0F0'],
    ['cyan', '0FF'],
    ['blue', '00F'],
    ['magenta', 'F0F'],
]

colours_dict = {name: rgb for name, rgb in colours}


def main():
    arg_dict = get_args()
    colour = arg_dict["colour"]

    rgb_code = get_rgb_code(colour)

    if rgb_code:
        print(f"The RGB code for {colour} is {rgb_code}")
    else:
        print(f"I don't know the RGB code for {colour}")

def get_args():
    parser = argparse.ArgumentParser(
        prog="rbg_colours",
        description="Display the RGB code for a corresponding colour"
    )

    parser.add_argument(
        "colour",
        help="the name of a colour",
        nargs="?",
        default="",
        type=str,
    )

    return vars(parser.parse_args())

def get_rgb_code(colour):
    # by default .get() returns None
    # when used in conditional statements, None evaluates to False
    return colours_dict.get(colour)

if __name__ == "__main__":
    main()

# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that users can also enter an RGB colour code, and be
#   told the name of the corresponding colour.
# * Change the program so that it ignores the case of the user's input.

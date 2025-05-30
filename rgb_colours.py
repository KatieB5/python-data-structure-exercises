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
import re

colours = [
    ['red', 'F00'],
    ['yellow', 'FF0'],
    ['green', '0F0'],
    ['cyan', '0FF'],
    ['blue', '00F'],
    ['magenta', 'F0F'],
]

colours_dict = dict(colours)


def main():
    arg_dict = get_args()
    arg = arg_dict["colour_or_rgb"]

    if get_rgb_code(arg):
        print(f"The RGB code for {arg} is {get_rgb_code(arg)}")

    elif is_arg_an_rgb_code(arg):
        colour = get_colour_from_rgb_code(arg.upper())
        if colour:
            print(f"The colour for RGB code {arg} is {colour}")
        else:
            print(f"I don't know the colour for RGB code {arg}")

    else:
        print(f"I don't know the RGB code for {arg}")

def get_args():
    parser = argparse.ArgumentParser(
        prog="rbg_colours",
        description="Display the RGB code for a corresponding colour, or display the colour for a corresponding RGB code"
    )

    parser.add_argument(
        "colour_or_rgb",
        help="the name of a colour or an RGB colour code",
        nargs="?",
        default="",
        type=str,
    )

    return vars(parser.parse_args())

def get_rgb_code(colour):
    return colours_dict.get(colour.lower())

def is_arg_an_rgb_code(arg):
    return bool(re.search('0', arg))

def get_colour_from_rgb_code(rgb_code):
    corresponding_colour = [k for k, v in colours_dict.items() if v == rgb_code]
    if corresponding_colour:
        return corresponding_colour[0]

if __name__ == "__main__":
    main()

# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that users can also enter an RGB colour code, and be
#   told the name of the corresponding colour.
# * Change the program so that it ignores the case of the user's input.

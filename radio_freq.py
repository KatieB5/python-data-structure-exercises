# This program knows about the frequencies of various FM radio stations in
# London.
#
# Usage:
#
# $ python radio_freq.py [station_name]
#
# For instance:
#
# $ python radio_freq.py "Radio 4"
# You can listen to Radio 4 on 92.5 FM
#
# or:
#
# $ python radio_freq.py "BBC Radio 5"
# I don't know the frequency of BBC Radio 5

import sys
import argparse

fm_frequencies = {
    "89.1 MHz": "BBC Radio 2",
    "91.3 MHz": "BBC Radio 3",
    "93.5 MHz": "BBC Radio 4",
    "94.9 MHz": "BBC London",
    "95.8 MHz": "Capital FM",
    "97.3 MHz": "LBC",
    "98.8 MHz": "BBC Radio 1",
    "100.0 MHz": "Kiss FM",
    "100.9 MHz": "Classic FM",
    "105.4 MHz": "Magic",
    "105.8 MHz": "Virgin",
    "106.2 MHz": "Heart 106.2",
}


def main():
    arg_dict = parse_args(sys.argv[1:])
    radio_station = arg_dict["radio_station"]
    for k, v in fm_frequencies.items():
        if v == radio_station:
            print(f"You can listen to {radio_station} on {k[:-4]} FM")
    else:
        print(f"I don't know the frequency of {radio_station}")
    # print("I know about {} FM radio stations".format(len(fm_frequencies)))


def parse_args(args):
    parser = argparse.ArgumentParser(
        prog="radio_freq",
        description="Display FM frequencies of known radio stations.",
    )
    parser.add_argument(
        "radio_station",
        help="the name of the radio station",
        type=str,
    )
    return vars(parser.parse_args(args))


if __name__ == "__main__":
    main()

# TODO:
# * Implement the program as described in the comments at the top of the file.

# TODO (extra):
# * Change the program so that if the radio station is not found, the user is
#   given a list of all stations that the program does know about.
# * Change the program so that if it is called without arguments, a table of
#   all radio stations and their frequencies is displayed.

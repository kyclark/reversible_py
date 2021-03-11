#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2021-03-11
Purpose: Find reversible words
"""

import argparse
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Find reversible words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='Words file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='/usr/share/dict/words')

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    seen = set()
    for line in args.file:
        for word in map(str.lower, filter(lambda w: len(w) > 2, line.split())):
            rev = ''.join(reversed(word[1:] + word[0]))
            if word == rev:
                if word not in seen:
                    print(word)
                    seen.add(word)


# --------------------------------------------------
if __name__ == '__main__':
    main()

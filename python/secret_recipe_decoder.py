#!/usr/bin/python3
import pydoc
import sys
import os

# Caesar encoding, for use with decoding below
ENCODING = {
    'y': 'a',
    'h': 'b',
    'v': 'c',
    'x': 'd',
    'k': 'e',
    'p': 'f',
    'z': 'g',
    's': 'h',
    'a': 'i',
    'b': 'j',
    'e': 'k',
    'w': 'l',
    'u': 'm',
    'q': 'n',
    'n': 'o',
    'l': 'p',
    'm': 'q',
    'f': 'r',
    'o': 's',
    'i': 't',
    'g': 'u',
    'j': 'v',
    't': 'w',
    'd': 'x',
    'r': 'y',
    'c': 'z',
    '3': '0',
    '8': '1',
    '4': '2',
    '0': '3',
    '2': '4',
    '7': '5',
    '5': '6',
    '9': '7',
    '1': '8',
    '6': '9'
}

"""An ingredient has an amount and a description.
For example: an Ingredient could have "1 cup" as the amount and "butter" as the description."""


class Ingredient():
    def __init__(self, amount, description) -> None:
        self.amount = amount
        self.description = description


def decode_string(str):
    """Given a string named str, use the Caesar encoding above to return the decoded string."""

    decoded_str = ""
    for char in str:
        if ENCODING.get(char) is None:
            decoded_str += char
        else:
            decoded_str += ENCODING.get(char)
    return decoded_str


def decode_ingredient(line):
    """Given an ingredient, decode the amount and description, and return a new Ingredient"""

    pcs = line.split('#')
    decoded_amt = decode_string(pcs[0])
    decoded_desc = decode_string(pcs[1])
    return Ingredient(decoded_amt, decoded_desc)


def main():
    """A program that decodes a secret recipe"""

    with open('decoded_recipe.txt', 'x') as decoded_recipe:
        with open('.\\secret_recipe.txt') as secret_recipe:
            for line in secret_recipe:
                decoded_line = decode_ingredient(line)
                decoded_line = ' '.join([decoded_line.amount, decoded_line.description])
                decoded_recipe.write(decoded_line)


if __name__ == "__main__":
    main()

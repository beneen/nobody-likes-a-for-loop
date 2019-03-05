"""
-----
Implement an algorithm to determine id a string has all unique characters.
-----
"""


def unique(s):
    return len(set(s)) == len(s)


if __name__ == "__main__":
    text = input("insert text:")
    print(unique(text))

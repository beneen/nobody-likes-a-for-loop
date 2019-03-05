"""
-----
Given two strings, write a method to decide if one is a permutation of the
other
-----
"""


def get_tuples_set(text):
    return set((elem, text.count(elem)) for elem in text)


def check_permutation(text1, text2):
    return get_tuples_set(text1) == get_tuples_set(text2)


if __name__ == "__main__":
    print(check_permutation(input("insert text1:"), input("insert text2:")))

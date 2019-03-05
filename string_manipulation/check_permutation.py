"""
-----
Given two strings, write a method to decide if one is a permutation of the
other
-----
"""


def get_tuples_list(text):
    list_of_tuples = [(elem, text.count(elem)) for elem in text]
    return list_of_tuples


def check_permutation(text1, text2):
    list_a = get_tuples_list(text1)
    list_b = get_tuples_list(text2)
    return set(list_a) == set(list_b)


if __name__ == "__main__":
    text1 = input("insert text1:")
    text2 = input("insert text2:")
    print(check_permutation(text1, text2))

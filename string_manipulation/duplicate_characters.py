"""
-----
print duplicate characters from string
-----
"""


def get_tuples_set(text):
    return set((elem, text.count(elem)) for elem in text)


def check_duplicate_characters(text):
    frequency_of_letters = list(filter(lambda x: x[1] > 1, get_tuples_set(text)))
    return''.join(([(a) for a, b in frequency_of_letters]))


def main():
    print(check_duplicate_characters(input("insert text1:")))


if __name__ == "__main__":
    main()
"""
-----
remove duplicate characters in a String
-----
"""


def remove_duplicate_characters(text):
    return ''.join([elem for elem in text if text.count(elem) == 1])


def main():
    print(remove_duplicate_characters(input("insert text1:")))


if __name__ == "__main__":
    main()
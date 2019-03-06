"""
-----
print first non repeated character from String

-----
"""



def first_non_repeated_character(text):
    return [x for x in text if text.count(x) == 1][0]


def main():
    print(first_non_repeated_character(input("insert text1:")))


if __name__ == "__main__":
    main()
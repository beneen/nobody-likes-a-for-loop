"""
-----
find duplicate characters in a String
-----
"""

def find_duplicate_characters(text):
    return set((elem, text.count(elem)) for elem in text if text.count(elem) != 1)


def main():
    print(find_duplicate_characters(input("insert text1:")))


if __name__ == "__main__":
    main()
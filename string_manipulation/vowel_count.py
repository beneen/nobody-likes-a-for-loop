"""
-----
vowel counter
-----
"""

def vowel_counter(text):
    return sum(list(map(text.count, "aeiou")))


def main():
    print(vowel_counter(input("insert text1:")))


if __name__ == "__main__":
    main()




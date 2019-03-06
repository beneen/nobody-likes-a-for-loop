"""
-----
check if two Strings are anagrams of each other

-----
"""



def check_anagram(text1, text2):
    return set((text1)) == set((text2))


def main():
    print(check_anagram(input("insert text1:"), input("insert text1:")))


if __name__ == "__main__":
    main()
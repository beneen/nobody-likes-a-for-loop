"""
-----
Assume you have a method isSubst ring which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat")
-----
"""

def string_rotation(string, possible_substring):
    return (len(string) == len(possible_substring) and string in possible_substring * 2)

def main():
    string = input("insert string:")
    possible_substring = input("insert possible substring:")
    print(string_rotation(string, possible_substring))

if __name__ == "__main__":
    main()

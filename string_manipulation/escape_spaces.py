"""
-----
Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string
-----
"""


def replace_characters(elem):
    if elem == " ":
        return "%20"
    else:
        return elem


def escape_spaces(s, n):
    if n != "":
        s = s[:-n]
    new_string = [replace_characters(elem) for elem in s]
    return ''.join(new_string)


if __name__ == "__main__":
    text = input("string with spaces:")
    n = int(input("number to trim by:"))
    print(escape_spaces(text, n))

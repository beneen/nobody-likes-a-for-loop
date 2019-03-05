"""
-----
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away
-----
"""


def characters_with_index(text):
    return set((x, text[x]) for x in range(0, len(text)))


def check_one_away(text1, text2):
    if abs(len(text1) - len(text2)) > 1:
        # more than one change is not allowed
        return False

    min_text = text1 if len(text1) <= len(text2) else text2
    max_text = text1 if len(text1) > len(text2) else text2

    max_characters = characters_with_index(max_text)
    min_characters = characters_with_index(min_text)
    differences = max_characters.difference(min_characters)

    sorted_differences = sorted(differences, key=lambda x: x[0])
    different_characters = ''.join([character for (_, character) in sorted_differences])
    return different_characters[1:] in min_text or different_characters[:-1] in min_text


if __name__ == "__main__":
    print(check_one_away(input("insert text1:"), input("insert text2:")))

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
    min_text = text1 if len(text1) <= len(text2) else text2
    max_text = text1 if len(text1) > len(text2) else text2

    max_characters = characters_with_index(max_text)
    min_characters = characters_with_index(min_text)
    difference = max_characters.difference(min_characters)

    if len(difference) > 1 and max_characters != min_characters:
        # cope with strings of the same length but different content
        return False

    if len(difference) >= 0 and not max_text.startswith(min_text):
        # possible insertion in the middle
        positions = sorted([x for (x, _) in difference])
        return positions[0] + len(positions) - 1 == positions[len(positions) - 1]
    elif len(difference) >= 1 and max_text.startswith(min_text):
        return False
    else:
        return True


if __name__ == "__main__":
    print(check_one_away(input("insert text1:"), input("insert text2:")))

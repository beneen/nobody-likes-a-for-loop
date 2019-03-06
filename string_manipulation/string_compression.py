"""
-----
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
-----
"""
from itertools import groupby

def string_compression(s):
    groups = groupby(s)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    text = "".join("{}{}".format(label, count) for label, count in result)

    if len(text) >= len(s):
        return s
    else:
        return text

if __name__ == "__main__":
    print(string_compression(input("insert text:")))


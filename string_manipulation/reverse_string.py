"""
-----
reverse a string

-----
"""



def reverse_string(text):
    return text[::-1]


def main():
    print(reverse_string(input("insert text1:")))


if __name__ == "__main__":
    main()
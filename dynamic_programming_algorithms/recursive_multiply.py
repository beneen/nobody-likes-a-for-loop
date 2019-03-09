"""
-----
Write a recursive function to multiply two positive integers without using the
* operator. You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.
-----
"""


def recursive_multiply(x, y):
    if x < 0:
        return recursive_multiply(-x, y)
    elif x == 0:
        return 0
    elif x == 1:
        return y
    else:
        return y + recursive_multiply(x - 1, y)


def main():
    print(recursive_multiply(int(input("number1:")), int((input("number2:")))))


if __name__ == "__main__":
    main()

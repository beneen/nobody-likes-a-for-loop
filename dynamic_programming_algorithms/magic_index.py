"""
-----
A magic index in an array A [e ... n -1] is defined to be an index such that A[ i] =
i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
"""


def characters_with_index(array):
    return list((x, array[x]) for x in range(0, len(array)))

def magic_index(array):
    return tuple(i == int(j) for i, j in characters_with_index(array))



def main():
    print(magic_index(list(input("sorted array:"))))


if __name__ == "__main__":
    main()

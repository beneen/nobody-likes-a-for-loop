"""
-----
Given an image represented by an NxN matrix, write a method to rotate the image by 90 degrees. can you do this in place?
-----
"""


def rotate_matrix(matrix):
    return [[matrix[row][column] for row in range(len(matrix) - 1, -1, -1)] for column in range(0, len(matrix[0]))]


def main():
    #hardcoded matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix(matrix))


if __name__ == "__main__":
    main()

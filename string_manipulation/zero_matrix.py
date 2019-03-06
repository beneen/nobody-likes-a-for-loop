"""
-----
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to O.
-----
"""

def zero_detection(matrix, row, column):
    return next((True for k in range(0, len(matrix)) if matrix[k][column] == 0 or matrix[row][k] == 0), False)


def zero_matrix(matrix):
    return [[0 if zero_detection(matrix, row, column) else matrix[row][column] for column in range(len(matrix))] for row in range(len(matrix))]


def main():
    #hardcoded matrix
    matrix = [[0, 2, 3], [4, 5, 0], [7, 0, 9]]
    print(zero_matrix(matrix))


if __name__ == "__main__":
    main()

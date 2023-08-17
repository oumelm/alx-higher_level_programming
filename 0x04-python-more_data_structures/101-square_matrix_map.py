#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(labda x: list(map(lambda i: i**2, x)), matrix))

#!/usr/bin/python3

"""Pascal's Triangle"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if i == 0:
            triangle.append(row)
            continue

        previous_row_index = i - 1

        for j in range(len(triangle[previous_row_index])):
            if j + 1 == len(triangle[previous_row_index]):
                row.append(1)
                break
            next_value = triangle[previous_row_index][j] + triangle[previous_row_index][j + 1]
            row.append(next_value)

        triangle.append(row)

    return triangle

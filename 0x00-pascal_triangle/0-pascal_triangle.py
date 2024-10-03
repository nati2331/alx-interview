#!/usr/bin/python3
"""Pascals Triangle"""

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for row_number in range(1, n):
        row = [1]
        for j in range(1, row_number):
            prev_row = triangle[row_number - 1]
            left = prev_row[j - 1]
            right = prev_row[j]
            element = left + right
            row.append(element)
        row.append(1)
        triangle.append(row)

    return triangle

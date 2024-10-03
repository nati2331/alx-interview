#!/usr/bin/python3
"""Pascals Triangle"""

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [[1]]
    for row_number in range(1, n):
        row = [1]
        for j in range(1, row_number):
            element = triangle[row_number - 1][j - 1] + triangle[row_number - 1][j]
            row.append(element)
        row.append(1)
        triangle.append(row)
    return triangle

if __name__ == "__main__":
    n = int(input("Enter the number of rows for Pascal's triangle: "))
    print(pascal_triangle(n))

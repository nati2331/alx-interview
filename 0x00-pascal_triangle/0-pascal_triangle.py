#!/usr/bin/python3
""" Pascal's Triangle """

def pascal_triangle(n):
    if n <= 0:
        return []

    result = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        result.append(row)
    return result

if __name__ == "__main__":
    try:
        # Prompt the user for input
        n = int(input("Enter the number of rows for Pascal's Triangle: "))
        # Print Pascal's Triangle
        print(pascal_triangle(n))
    except ValueError:
        print("Please enter a valid integer.")

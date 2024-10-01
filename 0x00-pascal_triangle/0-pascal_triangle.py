#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
    # Return an empty list if n <= 0
    if n <= 0:
        return []

    # Initialize the result list to hold all rows of Pascal's Triangle
    result = []

    # Iterate over each level from 0 to n-1
    for i in range(n):
        # Initialize the current row with all elements as 1
        row = [1] * (i + 1)
        
        # Fill in the middle elements of the row, if there are more than two elements
        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]
        
        # Append the current row to the result
        result.append(row)
    
    return result

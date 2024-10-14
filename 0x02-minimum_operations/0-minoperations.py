#!/usr/bin/python3
"""
Operations
"""

def minOperations(n):
    """
    returns int
    """
    if n <= 1:
        return 0
    for op in range(2, n+1):
        if n % op == 0:
            return minOperations(int(n/op)) + op

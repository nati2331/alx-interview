#!/usr/bin/python3
import sys

def print_solution(solution):
    """Print the solution in the required format."""
    print([[r, solution[r]] for r in range(len(solution))])

def is_safe(solution, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r in range(row):
        # Check column and diagonal attacks
        if solution[r] == col or abs(solution[r] - col) == abs(r - row):
            return False
    return True

def solve_nqueens(n, row=0, solution=[]):
    """Solve the N-Queens problem using backtracking."""
    if row == n:
        print_solution(solution)
    else:
        for col in range(n):
            if is_safe(solution, row, col):
                solution.append(col)
                solve_nqueens(n, row + 1, solution)
                solution.pop()  # Backtrack

def main():
    """Main function to handle input and initialize solving."""
    # Check argument count
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a valid integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem
    solve_nqueens(n)

if __name__ == "__main__":
    main()

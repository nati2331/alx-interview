#!/usr/bin/python3
"""Determines if all boxes can be unlocked."""


def canUnlockAll(boxes):
    """Evaluates if all boxes can be accessed.

    Args:
        boxes (list): List containing all boxes with their keys.

    Returns:
        bool: True if all boxes can be accessed, otherwise False.
    """
    n = len(boxes)
    
    opened = set([0])
    keys = set(boxes[0])
    
    while keys:
        new_keys = set()
        for key in keys:
            if key < n and key not in opened:
                opened.add(key)
                new_keys.update(boxes[key])
        keys = new_keys
        
    return len(opened) == n


def main():
    """Main execution function."""
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))


if __name__ == '__main__':
    main()

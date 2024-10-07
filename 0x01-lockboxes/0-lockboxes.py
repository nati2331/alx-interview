#!/usr/bin/python3

def canUnlockAll(boxes):
    # A list to track if a box has been opened
    opened = [False] * len(boxes)
    # Start with the first box
    opened[0] = True
    
    # Use a stack to keep track of boxes to explore
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        
        # Iterate through keys in the current box
        for key in boxes[current_box]:
            if key < len(boxes) and not opened[key]:
                # If the box has not been opened, open it
                opened[key] = True
                # Add it to the stack to explore its keys later
                stack.append(key)

    # If all boxes are opened, return True
    return all(opened)

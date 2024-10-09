#!/usr/bin/python3
"""Determines if all boxes can be unlocked."""


def find_next_open_box(opened_boxes):
    """Identifies the next opened box.
    
    Args:
        opened_boxes (dict): Dictionary of boxes that have been opened.
        
    Returns:
        list: Keys found in the opened box.
    """
    for index, box in opened_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Evaluates if all boxes can be accessed.
    
    Args:
        boxes (list): List containing all boxes with their keys.
        
    Returns:
        bool: True if all boxes can be accessed, otherwise False.
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    aux = {}
    while True:
        if len(aux) == 0:
            aux[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        keys = find_next_open_box(aux)
        if keys:
            for key in keys:
                try:
                    if aux.get(key) and aux.get(key).get('status') == 'opened/checked':
                        continue
                    aux[key] = {
                        'status': 'opened',
                        'keys': boxes[key]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in aux.values()]:
            continue
        elif len(aux) == len(boxes):
            break
        else:
            return False

    return len(aux) == len(boxes)


def main():
    """Main execution function."""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()

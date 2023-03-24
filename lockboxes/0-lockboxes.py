#!/usr/bin/python3
def canUnlockAll(boxes):
  """
    Determines whether all the boxes in a set of locked boxes can be opened.

    Args:
        boxes (list of lists): A list of n lists, where each list contains the keys to the other boxes. The boxes are numbered sequentially from 0 to n - 1.

    Returns:
        bool: True if all the boxes can be opened, False otherwise.
    """
    unlocked_boxes = [0]

    while True:
        unlocked_new_box = False

        for box in boxes:
            if boxes.index(box) in unlocked_boxes and boxes.index(box) not in unlocked_boxes:
                unlocked_boxes.append(boxes.index(box))
                unlocked_new_box = True
        
        if not unlocked_new_box:
            break

    if len(unlocked_boxes) == len(boxes):
        return True
    
    else:
        return False
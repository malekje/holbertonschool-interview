def canUnlockAll(boxes):

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
#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """  """
    unlocked_box = [boxes[0]]
    box_size = len(boxes)
    keys = [key for key in boxes[0]]

    for i in range(0, box_size):
        for key_ in keys:
            if key_ < len(boxes):
                if boxes[key_] not in unlocked_box:
                    for key_ in boxes[key_]:
                        if key_ not in keys:
                            keys.append(key_)
                    unlocked_box.append(boxes[key_])
    boxes.sort()
    unlocked_box.sort()
    if boxes == unlocked_box:
        return True
    else:
        return False

#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """  """
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    unlocked_box = [boxes[0]]
    keys = [key for key in boxes[0]]

    for i in range(0, len(boxes)):
        for key_ in keys:
            if key_ < len(boxes):
                if boxes[key_] not in unlocked_box:
                    for key__ in boxes[key_]:
                        if key__ not in keys:
                            keys.append(key__)
                    unlocked_box.append(boxes[key_])

    if len(boxes) == len(unlocked_box):
        return True
    else:
        return False

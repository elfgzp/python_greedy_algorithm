# -*- coding: utf-8 -*-
__author__ = 'gzp'


def can_jump(jump_array):
    """
    :param jump_array:
    :return:
    Given an array of integers, the elements in the array represent the farthest distance
    that can be jumped forward at the current position,
    and whether the given long jump strategy can jump to the last position.

    """
    if len(jump_array) == 0:
        return True

    max_jump = jump_array[0]

    last_steps = len(jump_array[1:])
    for location, jump_num in enumerate(jump_array[1:], start=1):
        if max_jump == 0:
            return False

        max_jump -= 1
        if max_jump < jump_num:
            max_jump = jump_num

        if max_jump + location > last_steps:
            return True

    return False


if __name__ == '__main__':
    array = [2, 3, 1, 1, 0]
    print (can_jump(array))

    array = [2, 3, 1, 1, 4]
    print (can_jump(array))

    array = [2, 0, 0, 4, 3]
    print (can_jump(array))

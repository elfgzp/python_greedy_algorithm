# -*- coding: utf-8 -*-
__author__ = 'gzp'


def max_sub_num_array_sum(num_array):
    """
    :param num_array: number array
    :return: max sub number array sum
    """
    assert isinstance(num_array, (list, tuple))
    assert len(num_array) > 0

    max_sum = num_array[0]
    current_max_sum = num_array[0]
    for num in num_array[1:]:
        current_max_sum += num
        if current_max_sum < 0:
            current_max_sum = 0
        if current_max_sum > max_sum:
            max_sum = current_max_sum

    if max_sum < 0:
        max_sum = max(num_array)

    return max_sum


if __name__ == '__main__':
    array = [-1, 1, -3, 4, -1, 2, 1, -5, 4]
    print (max_sub_num_array_sum(array))

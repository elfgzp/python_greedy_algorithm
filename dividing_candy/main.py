# -*- coding: utf-8 -*-
__author__ = 'gzp'


def dividing_candy(childs_height):
    """
    :param childs_height:a list of child height
    :return:
        Make sure that each child has at least one candy, and that the number of sweets
        that are higher than the neighbors is
        higher than that of his neighbors. According to this method of feeding,
        at least how many candies are needed.
    """
    assert len(childs_height) > 0
    candies_array = [1] * len(childs_height)

    index = 0
    last_height = childs_height[0]
    for next_height in childs_height[1:]:
        if next_height > last_height:
            candies_array[index + 1] = candies_array[index] + 1

        last_height = next_height
        index += 1

    candies_array.reverse()
    childs_height.reverse()
    index = 0
    last_height = childs_height[0]
    for next_height in childs_height[1:]:
        if next_height > last_height and candies_array[index + 1] <= candies_array[index]:
            candies_array[index + 1] = candies_array[index] + 1

        last_height = next_height
        index += 1

    candies_array.reverse()
    childs_height.reverse()

    print (childs_height)
    print (candies_array)

    candies = sum(candies_array)
    return candies


if __name__ == '__main__':
    array = [4, 2, 6, 8, 5]
    print (dividing_candy(array))

# Best : O(n*log n) - because we divide in half everytime even with big inputs it's kinda effective
# Avg : O(n*log n)
# Worst O(n*log n)
# Space worst : O(n)

# Trust me, you know as much as me what's happening here
# We write function that merges two sorted arrays, then put into that function recursivly merge_sort of left/right side of to_sort

import math

to_sort = [52, 63, 12, 6, 631, 6, 24, 637,
           64, 421, 74, 124, 0, -5, 523, -10, -529]


def merge_sort(arr: list):
    if len(arr) == 1:
        return arr
    mid = math.floor(len(arr)//2)
    left = arr[0:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    inx_left = 0
    inx_right = 0

    while inx_left < len(left) and inx_right < len(right):
        if left[inx_left] < right[inx_right]:
            result.append(left[inx_left])
            inx_left += 1
        else:
            result.append(right[inx_right])
            inx_right += 1
    return result + left[inx_left:] + right[inx_right:]


print(merge_sort(to_sort))

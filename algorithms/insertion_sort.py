# Best : O(n) - if sorted no need for insertions
# Avg : O(n^2)
# Worst O(n^2)
# Space worst : O(1) - in place

# Iterate throught list to sort, make elements before sorted and "insert" new elements at their intended places
# [1,2,5,4] => [1,2,5] [4] => [1,2,HERE 5] => take 5 and put it at j+1 so [1,2, ,5] =>
# j-1 in loop => put key at j+1 (it means at j, because we subtract 1) => [1,2,4,5]

to_sort = [52, 63, 12, 6, 631, 6, 24, 637,
           64, 421, 74, 124, 0, -5, 523, -10, -529]


def insertion_sort(arr: list):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j + 1] = key


insertion_sort(to_sort)
print(to_sort)

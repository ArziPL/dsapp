# Best : O(n*log n) - it can get very/bad good depends on good pivot point
# Avg : O(n*log n)
# Worst O(n^2)
# Space worst : O(log n) 

# We find some pivot point, and from that recursivly call quick_sort on left side of pivot point and right side
import math

to_sort = [52,63,12,6,631,6,24,637,64,421,74,124,0,-5,523,-10,-529]

def quick_sort(arr:list):
    if len(arr) <= 1:
        return arr
    else:
        left_side = []
        right_side = []
        pivot = arr[math.floor((len(arr)-1)/2)]
        
        for i in arr:
            if i < pivot:
                left_side.append(i)
            elif i > pivot:
                right_side.append(i)
        return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(to_sort))
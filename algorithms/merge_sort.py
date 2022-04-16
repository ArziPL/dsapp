import math

to_sort = [52,63,12,6,631,6,24,637,64,421,74,124,0,-5,523,-10,-529]

# Trust me, you know as much as me what's happening here

def merge_sort(arr:list): # O(n*Log n) - almost always the same time, because we divide in halves 
    if len(arr) == 1:
        return arr
    mid = math.floor(len(arr)//2)
    left = arr[0:mid]
    right = arr[mid:]
    return merge(merge_sort(left),merge_sort(right)) # Revursive merging every left/right 



def merge(left,right): # Sorting two sorted lists, which every is half of normal
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
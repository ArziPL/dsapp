to_sort = [52,63,12,6,631,6,24,637,64,421,74,124,0,-5,523,-10,-529]

def insertion_sort(arr:list):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]: # find value j that is minimally bigger then key,
            arr[j+1] = arr[j]          # put that j at j+1 and then at j put key (a[j+1] = a[j] because we first subtract 1)
            j = j - 1
        arr[j + 1] = key # almost like arr[j]

insertion_sort(to_sort)
print(to_sort)




















def insertion_sort(arr:list):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]: # find value j that is minimally bigger then key,
            arr[j+1] = arr[j]          # put that j at j+1 and then at j put key (a[j+1] = a[j] because we first subtract 1)
            j = j - 1
        arr[j + 1] = key # almost like arr[j]
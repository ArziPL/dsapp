# Avg O(log(n)), worst when value at end of list/outside of list

# Take sorted list and check if searched value is greater/lower then 
# middle value (floor avg), then cut other half of list, and repeat 
# unitl there's 1 element


import math

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def binary_search(arr:list,num):
    min = 0
    max = len(arr) - 1
    avg = 0

    while min <= max:
        avg = math.floor((min+max)//2)
        print(min,max,sep=", ",end="\n")
        
        if num > arr[avg]:
            min = arr.index(arr[avg])+1
        elif num < arr[avg]:
            max = arr.index(arr[avg])-1
        else:
            return avg
    return False
        
print("Ans : ",binary_search(primes,83),primes.index(83),end="\n\n\n")
print("Ans : ",binary_search(primes,29),primes.index(29),end="\n\n\n")
print("Ans : ",binary_search(primes,37),primes.index(37),end="\n\n\n")
print("Ans : ",binary_search(primes,2),primes.index(2),end="\n\n\n")
print("Ans : ",binary_search(primes,97),primes.index(97),end="\n\n\n")
print("Ans : ",binary_search(primes,3),primes.index(3),end="\n\n\n")
print("Ans : ",binary_search(primes,89),primes.index(89),end="\n\n\n")
print("Ans : ",binary_search(primes,-5),end="\n\n\n")
print("Ans : ",binary_search(primes,103),end="\n\n\n")

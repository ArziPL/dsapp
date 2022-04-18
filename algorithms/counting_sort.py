# Best : O(n + k)
# Avg : O(n + k)
# Worst O(n + k)
# Space worst : O(k) - CAN GET VERY BIG BIG

# k - range of values in array

# Take every number in arr then add += 1 to index of that number in temporary arrays, then
# for every index in temporary arrays add to final_arr that amount of that index number of 
# how big number at that index is - if arr[23] = 3 then add 23 23 23 and same for negatives
# 1. The whole thing can get very ineffective if numbers in arr are big
# 2. Possibility of sorting negatives greatly increase time/space complexity
#     create array len of min(to_sort), do the same as positives, then for final result multiply by -1 to get negatives
#     and reverse them because we were counting them as positive => [1,5,10] => [-1,-5,-10] => [-10,-5,-1] and
#     add that array at beginning of positive_sorted

to_sort = [52, 63, 12, 6, 631, 6, 24, 637,
           64, 421, 74, 124, 0, -5, 523, -10, -529]


def counting_sort(arr: list):

    positive_list = [0] * (max(arr)+1)
    negative_list = [0] * (-1*(min(arr)-1))
    final_positive = []
    final_negative = []

    for i in arr:
        if i < 0:
            ti = -i
            negative_list[ti] += 1
        else:
            positive_list[i] += 1

    for inx, i in enumerate(positive_list):
        final_positive.append(i*[inx])
    for inx, i in enumerate(negative_list):
        final_negative.append(i*[-inx])

    final_negative.reverse()
    return [num for sublist in final_negative + final_positive for num in sublist]


print(counting_sort(to_sort))

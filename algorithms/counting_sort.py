# Best : O(n + k)
# Avg : O(n + k)
# Worst O(n + k)
# Space worst : O(k) - CAN GET VERY BIG BIG
# k - range of values in array
# The whole thing can get very ineffective if numbers in arr 
# are big, even more ineffective if we sort negatives as well 

to_sort = [52,63,12,6,631,6,24,637,64,421,74,124,0,-5,523,-10,-529]

def counting_sort(arr:list): # Possibility of sorting negatives greatly increase time/space complexity


    positive_list = [0] * (max(to_sort)+1)
    negative_list = [0] * (-1*(min(to_sort)-1))
    final_positive = []
    final_negative = []


    for i in to_sort: # At every array index add 1 if value in to_sort exists
        if i < 0:
            ti = -i
            negative_list[ti] += 1
        else:
            positive_list[i] += 1
    

    # For every index add to final_arr that amount of that index number of how big number at that index is 
    # if arr[23] = 3 then add 23 23 23 and same for negatives
    for inx,i in enumerate(positive_list):
            final_positive.append(i*[inx])
    for inx,i in enumerate(negative_list):
            final_negative.append(i*[-inx])
    

    final_negative.reverse() # Reverse negatives because we were counting them as positive [1, 5, 10] for pos will be as [-10, -5, -1]
    return [num for sublist in final_negative + final_positive for num in sublist] # Flatten the list of lists

print(counting_sort(to_sort))

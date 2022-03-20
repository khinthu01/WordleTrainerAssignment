def counting_sort(arr):
    # grabbing the max value in input and initialising a list with a length = max value of input
    max_val = max(arr)
    count_arr = [0]*max_val

    # storing the count of each element in input arr in count_arr
    for num in arr:
        count_arr[num-1] += 1

    # changing count_arr to store the positions of the last element of a specific key in the sorted array (i.e if at count_arr[1] = 5 then the last occurence of 2 in sorted_arr will be at index 4)
    for i in range(1,max_val):
        count_arr[i] += count_arr[i-1]

    # placing values from arr into a sorted array (sorted_arr)
    # done by iterating through arr from the right (to maintain stability)
    # elements are accessed and then the element is used to find the count/position of the last element in count_arr and then placed into sorted_arr based on that position
    sorted_arr = [0]*len(arr)
    for i in range(len(arr)-1, -1, -1):
        n = arr[i]
        sorted_arr[count_arr[n-1]-1] = n
        count_arr[n-1] -= 1

    return sorted_arr
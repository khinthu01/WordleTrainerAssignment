def counting_sort(arr, position):
    # creating a counting array of length 26 for each of the 26 characters using the ord() function to get the Unicode codes
    min_val = ord('a')
    max_val = ord('z')
    val_range = max_val - min_val + 1
    count_arr = [0]*val_range

    # storing the count of each element in input arr in count_arr using the Unicode code of the letter at the position in the string element in arr
    for word in arr:
        letter = word[position]
        count_arr[ord(letter)-min_val] += 1

    # changing count_arr to store the positions of the last element of a specific key in the sorted array (i.e if at count_arr[1] = 5 then the last occurence of the letter represented at index 1 in sorted_arr will be at index 4)
    for i in range(1,val_range):
        count_arr[i] += count_arr[i-1]

    # placing values from arr into a sorted array (sorted_arr)
    # done by iterating through arr from the right (to maintain stability)
    # elements are accessed and then the element is used to find the count/position of the last element in count_arr and then placed into sorted_arr based on that position
    length = len(arr)
    sorted_arr = [0]*length
    for i in range(length-1, -1, -1):
        word = arr[i]
        letter = word[position]
        n = ord(letter)
        sorted_arr[count_arr[n-min_val]-1] = word
        count_arr[n-min_val] -= 1

    return sorted_arr


def radix_sort(arr):
    word_length = len(arr[0])

    for i in range(word_length-1, -1, -1):
        sorted_arr = counting_sort(arr, i)

    return sorted_arr

def right_binary_search(arr, target):
    lo = 0
    hi = len(arr)

    while (lo < hi - 1):
        mid = (lo + hi) //2
        if target >= arr[mid]:
            lo = mid
        elif target < arr[mid]:
            hi = mid
    
    if arr[lo] == target:
        return lo
    
    return False

def left_binary_search(arr, target):
    lo = 0
    hi = len(arr)

    while (lo < hi - 1):
        mid = (lo + hi) //2
        if target > arr[mid]:
            lo = mid
        elif target <= arr[mid]:
            hi = mid
    
    if arr[hi] == target:
        return hi
    
    return False
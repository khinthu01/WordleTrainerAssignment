def counting_sort(arr):
    # extracting the Unicode code of the minimum and maximum letter in the array and using that to determine the required length of the count_arr where we will store the count of each letter
    min_val = ord(min(arr))
    max_val = ord(max(arr))
    val_range = max_val - min_val + 1
    count_arr = [0]*val_range

    # storing the count of each element in input arr in count_arr
    for letter in arr:
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
        n = ord(arr[i])
        sorted_arr[count_arr[n-min_val]-1] = chr(n)
        count_arr[n-min_val] -= 1

    return sorted_arr


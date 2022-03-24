# code for Task 1 in Assignment 1
# This file contains the python code for a Wordle Trainer
# Author: Khin Moe Thu Kyaw
# Student Id: 28751639

def counting_sort(arr, position):
    '''
    This function sorts an array of strings in a non-decreasing order based on the letter at position using a non-comparison sorting algorithm.

    :param arr: an array of strings are the same length and all characters are letters of the English alphabet
    :param position: position of the letter in the string that the array is supposed to sort on. For example, if position is 5 then the function will sort based on the sixth letter in all string elements in arr.

    :returns: a sorted array

    :time complexity: counting_sort has a time complexity of O(n*k) where n is the length of arr and k is the number of different letters in the alphabet. Since k is constant at 26 this results in an overall worst-case time complexity of O(n).
    :space complexity: counting_sort has a space complexity of O(n) where n is the length of the sorted array which equals to the length of arr. 
    '''

    # creating a counting array of length 26 for each of the 26 characters using the ord() function to get the Unicode codes
    min_val = ord('a')
    max_val = ord('z')
    val_range = max_val - min_val + 1
    count_arr = [0]*val_range

    # storing the count of each element in input arr in count_arr using the Unicode code of the letter at the position in the string element in arr
    for word in arr:
        word = word.lower()
        letter = word[1][position]
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
        letter = word[1][position]
        n = ord(letter)
        sorted_arr[count_arr[n-min_val]-1] = word
        count_arr[n-min_val] -= 1

    return sorted_arr


def radix_sort(arr):
    word_length = len(arr[0][0])
    sorted_arr = arr

    for i in range(word_length-1, -1, -1):
        sorted_arr = counting_sort(sorted_arr, i)

    return sorted_arr

def right_binary_search(arr, target):
    lo = 0
    hi = len(arr)

    while (lo < hi - 1):
        mid = (lo + hi) //2
        word = arr[mid]
        if target >= word[1]:
            lo = mid
        elif target < word[1]:
            hi = mid

    if arr[lo][1] == target:
        return lo
    
    return False

def left_binary_search(arr, target):
    lo = 0
    hi = len(arr)

    while (lo < hi - 1):
        mid = (lo + hi) //2
        word = arr[mid]
        if target > word[1]:
            lo = mid
        elif target <= word[1]:
            hi = mid
        

    if arr[lo][1] == target:
        return lo
    
    return False

def sort_word(word):
    # creating a counting array of length 26 for each of the 26 characters using the ord() function to get the Unicode codes
    min_val = ord('a')
    max_val = ord('z')
    val_range = max_val - min_val + 1
    count_arr = [0]*val_range

    # storing the count of each letter in word in count_arr where the count of the letter is stored at the index ord(letter) - min_val
    for letter in word:
        count_arr[ord(letter)-min_val] += 1

    # changing count_arr to store the positions of the last occurrence of a specific letter in the sorted word array (i.e if at count_arr[1] = 5 then the last occurence of the letter represented at index 1 in sorted_arr will be at index 4)
    for i in range(1,val_range):
        count_arr[i] += count_arr[i-1]

    # placing letters from word into a sorted word array (sorted_word)
    # done by iterating through arr from the right (to maintain stability)
    # elements are accessed and then the element is used to find the count/position of the last occurrence of the element in count_arr and then placed into sorted_word based on that position
    length = len(word)
    sorted_word = [0]*length
    for i in range(length-1, -1, -1):
        letter = word[i]
        n = ord(letter)
        sorted_word[count_arr[n-min_val]-1] = letter
        count_arr[n-min_val] -= 1

    return sorted_word

def trainer(wordlist, word, marker):


    # if marker shows that all 1's then the word is already correct - best case complexity is O(1)
    if marker == [1]*len(marker):
        return [word]

    # using a list of tuples to store words along with their key to allow for the grouping of anagrams
    tuple_list = []

    # a loop to created the tuple list O(nm) since the counting sort can be used to sort the word at O(m) complexity where m is the number of letters in elem
    # space complexity is O(n)
    for elem in wordlist:
        elem.lower()
        key = "".join(sort_word(elem)) 
        tuple_list.append((elem, key))

    #radix_sort of tuple list by anagram key
    sorted_list = radix_sort(tuple_list)

    #getting list of anagrams of input word
    anagram = "".join(sort_word(word))
    left_anagram = left_binary_search(sorted_list, anagram)
    right_anagram = right_binary_search(sorted_list, anagram)

    anagrams = sorted_list[left_anagram:right_anagram+1]
    anagram_words = []

    # making a list of only the anagrams in anagram word without the key
    for elem in anagrams: 
        anagram_words.append(elem[0])

    valid_anagrams = []

    #looping through marker and anagram_words to find words that fit the criteria of having different letters in spots where marker[i] == 0 and having the same letter as input word in spots where marker[i] == 1
    # worst case time complexity = O(nm) where anagram_words is the same length as wordlist and n is the length of wordlist and m is the length of each word in wordlist
    for i in range(len(marker)):
        for j in range(len(anagram_words)):
            if marker[i] == 0 and anagram_words[j][i] != word[i]:
                valid_anagrams.append(anagram_words[j])
            if marker[i] == 1 and anagram_words[j][i] == word[i]:
                valid_anagrams.append(anagram_words[j])
        
        anagram_words = valid_anagrams
        valid_anagrams = []
    
    return anagram_words




# li = [('pears', 'aeprs'), ('apple','aelpp'), ('ablet', 'abelt'), ('parse', 'aeprs')]


# print(radix_sort(li))

# sorted_li = radix_sort(li)
# print(right_binary_search(sorted_li, 'aeprs'))
# print(left_binary_search(sorted_li, 'aeprs'))

wordlist = ["limes", "spare", "store", "pares",
"pears", "stare", "spear", "parse", "reaps"]
word = "pares"
marker = [1, 0, 0, 0, 1]

print(trainer(wordlist, word, marker))

print(sort_word('pares'))
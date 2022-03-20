from numpy import sort


def counting_sort(arr, position):
    # creating a counting array of length 26 for each of the 26 characters using the ord() function to get the Unicode codes
    min_val = ord('a')
    max_val = ord('z')
    val_range = max_val - min_val + 1
    count_arr = [0]*val_range

    # storing the count of each element in input arr in count_arr using the Unicode code of the letter at the position in the string element in arr
    for word in arr:
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

def trainer(wordlist, word, marker):
    if marker == [1]*len(marker):
        return [word]

    tuple_list = []

    for elem in wordlist:
        elem.lower()
        key = "".join(sorted(elem))
        tuple_list.append((elem, key))

    #radix_sort
    sorted_list = radix_sort(tuple_list)

    #getting list of anagrams
    anagram = "".join(sorted(word))
    left_anagram = left_binary_search(sorted_list, anagram)
    right_anagram = right_binary_search(sorted_list, anagram)

    anagrams = sorted_list[left_anagram:right_anagram+1]
    anagram_words = []

    for elem in anagrams: 
        anagram_words.append(elem[0])

    valid_anagrams = []

    #eliminating them if they have values in certain spots
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
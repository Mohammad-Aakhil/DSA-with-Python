def first_non_repeating_char(s):
    # Step 1: count frequencies
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    # Step 2: find first char with count == 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None  # if no non-repeating char exists


# Example
# print(first_non_repeating_char("swiss"))   # Output: w
# print(first_non_repeating_char("aabbcc"))  # Output: None
# print(first_non_repeating_char("leetcode")) # Output: l


from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)   # key = sorted word, value = list of words
    
    for word in strs:
        key = ''.join(sorted(word))   # sort word to make key
        anagram_map[key].append(word)
    
    return list(anagram_map.values())


# Example
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


# list = ["ant", "tea", "eat"]
# anagram_map = defaultdict(list)   # key = sorted word, value = list of words
# # print(anagram_map)



def group_anagrams(strings_list):
    anagram = {}

    for word in strings_list:
        key = "".join(sorted(word))

        if key not in anagram:
            anagram[key] = []
        anagram[key].append(word)

    return anagram.values()

# print(group_anagrams(["ant", "cat", "rat", "mat", "sat", "art"]))


def two_array(arr, tar):
    tg_index = []
    tg_subarr_sum = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == tar:
                tg_index.append([i,j])
                tg_subarr_sum.append([arr[i], arr[j]])
    print(tg_subarr_sum)
    return tg_index


print(two_array([3,6,4,7,5,2,9,8], 9) )           


list_1 = [1,2,2,3,4,4,5,6,7,7,8,99,99]
list_1 = {list_1}
print(list_1)



def is_unique_str(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True


print(is_unique_str("unq"))
print(is_unique_str("pavan"))


def is_unq(s):
    return len(s) == len(set(s))

print(is_unq('uniqe'))
print(is_unq('dummy'))

def longest_repeting_seq(arr):
    return

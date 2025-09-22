class Hash_map:
    def __init__(self, capacity):
        self.hash_table = [None]*capacity
        self.capacity = 10
        self.table = [None] * capacity 

    def hash(self, key):
        return hash(key) % self.capacity
    
    def insert(self, key, value):
        index = self.hash(key)

        if self.table[index] is None:
            self.table[index] = []

        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = [key, value]
                return         
        else:
            self.table[index].append([key, value])


    def get_value_by_key(self, key):
        index = self.hash(key)
        bucket = self.table[index]

        for k,v in bucket:
            if k == key:
                return v
            else:
                return "empty bucket"


    def get_all_keys(self):
        all_keys = []
        for buckets in self.table:
            if buckets is None:
                continue
            for k,_ in buckets:
                all_keys.append(k)
        return all_keys


    def get_all_values(self):
        all_values = []  
        for buckets in self.table:
            if buckets is None:
                continue
            for _,v in buckets:
                all_values.append(v)
        return all_values
    

    def get_filled_buckets(self):
        filled_buckets = []
        for buckets in self.table:
            if buckets is None:
                continue
            for k,v in buckets:
                filled_buckets.append([k,v])
        return filled_buckets


            

# h = Hash_map(10)
# print(h.table)
# h.insert("chappal", 2 )
# h.insert("shoe", 4 )
# h.insert("shoe", 3 )
# h.insert("watch", 3)
# print(h.table)
# print(h.get_value_by_key("shoe"))
# print(h.get_all_keys())
# print(h.get_all_values())
# print(h.get_filled_buckets())

# d = {'a':1, 'b':2, 'c':3}
# print(d.keys())
# print(d.values())
# print(type(d))

# l=list(d)
# print(list(d.items())[0])


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


# from collections import defaultdict

# def groupAnagrams(strs):
#     anagram_map = defaultdict(list)   # key = sorted word, value = list of words
    
#     for word in strs:
#         key = ''.join(sorted(word))   # sort word to make key
#         anagram_map[key].append(word)
    
#     return list(anagram_map.values())


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


# print(two_array([3,6,4,7,5,2,9,8], 9) )           


# list_1 = [1,2,2,3,4,4,5,6,7,7,8,99,99]
# list_1 = {list_1}
# print(list_1)

# def is_unique_str(string):
#     for i in range(len(string)):
#         for j in range(i+1, len(string)):
#             if string[i] == string[j]:
#                 return False
#     return True


# print(is_unique_str("unq"))
# print(is_unique_str("pavan"))


def is_unq(s):
    return len(s) == len(set(s))

print(is_unq('uniqe'))
print(is_unq('dummy'))

def longest_repeting_seq(arr):
    return

        
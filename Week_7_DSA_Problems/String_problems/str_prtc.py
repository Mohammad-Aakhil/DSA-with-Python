def anagram_check(str_1, str_2):
    if sorted(str_1) == sorted(str_2):
        return True
    return False
print(anagram_check('ant', 'ton'))


def group_anagrams(list):
    anagrams = {}
    for word in list:
        key = "".join(sorted(word))

        if key not in anagrams:
            anagrams[key] = []
            anagrams[key].append(word)
            
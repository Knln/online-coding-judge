from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {}

        if len(strs) == 0:
            return [[]]
        elif len(strs) == 1:
            return [strs]

        for word in strs:
            key = [x-x for x in range(0, 26)]
            for letter in word:
                key[ord(letter) - 97] += 1

            key_tuple = tuple(key)
            if key_tuple in anagram_dict.keys():
                anagram_dict[key_tuple].append(word)
            else:
                anagram_dict[key_tuple] = []
                anagram_dict[key_tuple].append(word)

        answer = [value for value in anagram_dict.values()]

        return answer


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(["e"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["", "w", "wap", "paw", "pawpaw"]))
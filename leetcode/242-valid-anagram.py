class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = {}

        if len(s) == 0 and len(t) == 0:
            return True
        elif len(s) != len(t):
            return False

        for letter in s:
            if letter not in anagram_dict.keys():
                anagram_dict[letter] = 1
            else:
                anagram_dict[letter] += 1

        for letter in t:
            if letter not in anagram_dict.keys():
                return False
            else:
                anagram_dict[letter] -= 1

            if anagram_dict[letter] < 0:
                return False

        return True


print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("rat", "car"))
print(Solution().isAnagram("rat", "ra"))
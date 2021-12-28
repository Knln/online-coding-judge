from typing import List
from collections import defaultdict


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        if not dictionary:
            return sentence

        if not sentence:
            return ""

        list_of_words = sentence.split(' ')
        lookup_dict = defaultdict()

        for w in dictionary:
            lookup_dict[w] = 1

        for i, word in enumerate(list_of_words):
            check_string = ""
            j = 0
            for char in word:
                j += 1
                check_string += char
                if check_string in lookup_dict:
                    break

            if j != len(word):
                list_of_words[i] = check_string

        return " ".join(list_of_words)


solution = Solution()
print(solution.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
print(solution.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))
print(solution.replaceWords(dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
print(solution.replaceWords(dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
print(solution.replaceWords(dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"))

from collections import defaultdict
from typing import List
import re


class Solution:

    def remove_non_letters(self, string: str):
        return re.sub('[\W]', ' ', string)

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        word_frequency = defaultdict()
        paragraph = self.remove_non_letters(paragraph)

        for word in paragraph.split():
            if word.lower() in word_frequency.keys():
                word_frequency[word.lower()] += 1
            else:
                word_frequency[word.lower()] = 1

        tuple_of_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

        for word in tuple_of_words:
            if word[0] in banned:
                continue
            else:
                return word[0]


if __name__ == "__main__":
    solution = Solution()
    print(solution.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit", ["hit"]))

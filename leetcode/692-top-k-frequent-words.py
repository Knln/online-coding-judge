from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        dictionary = Counter(words)

        ordered = sorted(dictionary.items(), key=lambda a: (-a[1], a[0]))
        answer = ordered[0:k]

        return [x[0] for x in answer]

solution = Solution()
print(solution.topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2))
print(solution.topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4))
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:

        d = Counter(s)
        string = ""

        for t in d.most_common():
            string += t[0] * t[1]

        return string

solution = Solution()
print(solution.frequencySort(s="zftreedff"))
import re

class Solution:
    def remove_non_letters(self, string: str) -> str:
        return re.sub('[\W]', ' ', string)

    def lengthOfLastWord(self, s: str) -> int:
        if s == "" or s.strip() == "":
            return 0

        s = self.remove_non_letters(s)
        last_word = s.split()

        return len(last_word)

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord("Bob hit a ball, the hit BALL flew far after it was hit"))
    print(solution.lengthOfLastWord(" "))
    print(solution.lengthOfLastWord("B"))
    print(solution.lengthOfLastWord(""))

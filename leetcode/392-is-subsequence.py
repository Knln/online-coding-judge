class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s:
            return True
        elif not t:
            return False

        count_t = 0
        count_s = 0

        while count_s < len(s) and count_t < len(t):
            if s[count_s] == t[count_t]:
                count_s += 1
                count_t += 1
            else:
                count_t += 1

        if count_s != len(s):
            return False
        else:
            return True
import re

from application.lib.request import Request
from .request import Request
from .request import Conf

from application.lib import Request

class Solution:
    def myAtoi(self, s: str) -> int:
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31

        s = s.strip()
        regex = r'[\-\+]?\d+'

        s = re.match(regex, s)
        if not s:
            return 0
        else:
            return min(int_max, max(int(s.group()), int_min))


print(Solution().myAtoi("words and 987"))
print(Solution().myAtoi("4193 with words"))
print(Solution().myAtoi("   -42"))
print(Solution().myAtoi("-91283472332"))
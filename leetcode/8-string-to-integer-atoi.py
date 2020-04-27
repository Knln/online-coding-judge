"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as
possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231)
is returned.
"""
import re

class Solution:
    def myAtoi(self, str: str) -> int:

        int_max = 2**31-1
        int_min = -2**31
        val = 0
        sign = 1

        str_trunc = str.strip()
        regex = re.match(r'^[\-\+]?\d+', str_trunc)

        if regex:
            str_trunc = regex.group()
        else:
            return 0

        if str_trunc[0] == '-':
            sign = -1
            str_trunc = str_trunc[1:]
        elif str_trunc[0] == '+':
            sign = 1
            str_trunc = str_trunc[1:]

        str_length = len(str_trunc)

        for i in range(str_length):
            if sign*int(str_trunc) > int_max:
                val = int_max
            elif sign*int(str_trunc) < int_min:
                val = int_min
            else:
                val = sign*int(str_trunc)

        return val


if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.myAtoi("423")))
    print("{}".format(solution.myAtoi("   -42")))
    print("{}".format(solution.myAtoi("4193 with words")))
    print("{}".format(solution.myAtoi("words and 991")))
    print("{}".format(solution.myAtoi("-91283472332")))
    print("{}".format(solution.myAtoi("    ")))


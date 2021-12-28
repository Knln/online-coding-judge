"""
Given a 32-bit signed integer, reverse digits of an integer.
"""

class Solution:
    def reverse(self, x: int) -> int:

        int_max = 2**31-1
        int_min = -2**31
        sign = 1

        x_str = str(x)

        if x_str[0] == '-':
            sign = -1
            x_str = x_str[1:]

        x_rev = int(x_str[-1::-1])

        if sign*x_rev < int_min or sign*x_rev > int_max:
            x_rev = 0
        else:
            x_rev = sign*x_rev

        return x_rev

if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.reverse(122)))
    print("{}".format(solution.reverse(120)))
    print("{}".format(solution.reverse(-492)))
    print("{}".format(solution.reverse(-11)))
    print("{}".format(solution.reverse(0)))
    print("{}".format(solution.reverse(1)))
    print("{}".format(solution.reverse(992102927472988)))
    print("{}".format(solution.reverse(-992102927472988)))


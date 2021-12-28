
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        int_max = 2**31-1
        int_min = -2**31

        if divisor == 0 or dividend == 0:
            return 0

        if divisor == 1:
            return min(int_max, max(dividend, int_min))

        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        else:
            sign = -1

        dividend_s, divisor_s = abs(dividend), abs(divisor)
        count = -1
        quotient = 0

        while divisor_s <= dividend_s:
            divisor_s = divisor_s << 1
            count = count + 1
        divisor_s = divisor_s >> 1

        while count > -1:
            if dividend_s >= divisor_s:
                quotient += (1 << count)
                dividend_s -= divisor_s
            divisor_s = divisor_s >> 1
            count = count - 1

        quotient = sign*quotient

        if quotient > int_max or quotient < int_min:
            quotient = int_max

        return quotient


if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.divide(9, 3)))  # 3
    print("{}".format(solution.divide(10, 3)))  # 3
    print("{}".format(solution.divide(7, -3)))  # -2
    print("{}".format(solution.divide(-27, 3)))  # -9
    print("{}".format(solution.divide(1, 0)))  # 0 (should be undefined)
    print("{}".format(solution.divide(0, 1)))  # 0
    print("{}".format(solution.divide(3, 3)))  # 1
    print("{}".format(solution.divide(3, 10)))  # 0
    print("{}".format(solution.divide(1, 2)))  # 0
    print("{}".format(solution.divide(2147483647, 1)))  # int_max
    print("{}".format(solution.divide(-2147483648, 1)))  # int_min
    print("{}".format(solution.divide(2, -2147483649)))  # 0
    print("{}".format(solution.divide(-3, -3)))  # 1
    print("{}".format(solution.divide(-3, 3)))  # -1

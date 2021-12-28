class Solution:
    def scoreOfParentheses(self, S: str) -> int:

        stack = [0]
        answer = 0

        for s in S:
            print(stack)
            if len(stack) == 1:
                answer += stack[0]

            if s == '(':
                stack.append(0)
            else:
                m = stack.pop()
                if m == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2*m

        return stack[0]

solution = Solution()
print(solution.scoreOfParentheses("((()))"))
print(solution.scoreOfParentheses("()()()"))
print(solution.scoreOfParentheses("()(())"))
print(solution.scoreOfParentheses("(()(()))"))
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dictionary = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = list()

        for c in s:
            if c in bracket_dictionary.values():
                stack.append(c)
            elif c in bracket_dictionary.keys():
                if not stack:
                    return False
                else:
                    removed_c = stack.pop()
                    if bracket_dictionary[c] == removed_c:
                        continue
                    else:
                        return False
            else:
                return False

        if stack:
            return False
        else:
            return True



if __name__ == "__main__":
    solution = Solution()
    print("{}".format(solution.isValid("")))
    print("{}".format(solution.isValid(")")))
    print("{}".format(solution.isValid("(]")))
    print("{}".format(solution.isValid("{[]}")))
    print("{}".format(solution.isValid("([)]")))

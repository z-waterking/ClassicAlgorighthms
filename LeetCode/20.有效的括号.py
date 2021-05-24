#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) != 0:
                    if c == ')' and stack[-1] == '(' \
                        or c == '}' and stack[-1] == '{' \
                            or c == ']' and stack[-1] == '[':
                            stack.pop()
                    else:
                        return False
                else:
                    return False

        if len(stack) != 0:
            return False

        return True

# @lc code=end


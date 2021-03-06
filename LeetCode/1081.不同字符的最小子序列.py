#
# @lc app=LeetCode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        
        stack = []
        exist_set = {}

        for c in s:
            # 先减1
            count[c] -= 1
            if exist_set.get(c) == True:
                continue

            while len(stack) > 0 and c < stack[-1]:
                # 如果后面没了，就不要删
                if count[stack[-1]] == 0:
                    break
                exist_set[stack.pop()] = False
                
            # 加入栈中
            stack.append(c)
            exist_set[c] = True
        
        return "".join(stack)
# @lc code=end


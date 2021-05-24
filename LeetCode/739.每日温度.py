#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 用单调栈的思想去解决
        # 从后往前遍历
        res = [0] * len(temperatures)
        
        stack = []
        # 从后往起前遍历
        for tp_index in range(len(temperatures)-1, -1, -1):
            # 单调增栈
            # 元素入栈前，需要进行比较
            # 如果比栈顶元素大，则T掉栈顶元素，自己入栈，
            # 否则，直接入栈
            while len(stack) != 0 and temperatures[stack[-1]] <= temperatures[tp_index]:
                stack.pop()

            if len(stack) == 0:
                res[tp_index] = 0
            else:
                res[tp_index] = stack[-1] - tp_index

            stack.append(tp_index)
            
        return res
                
# @lc code=end


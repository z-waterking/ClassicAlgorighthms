#
# @lc app=leetcode.cn id=769 lang=python3
#
# [769] 最多能完成排序的块
#

# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        cur_max = 0

        for i in range(len(arr)):
            cur_max = max(cur_max, arr[i])
            if cur_max == i:
                res += 1
        
        return res
# @lc code=end


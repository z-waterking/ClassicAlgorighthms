#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        farthest = 0
        jumps = 0
        for i in range(n-1):
            farthest = max(nums[i] + i, farthest)

            if end == i:
                jumps += 1
                end = farthest

        return jumps;
# @lc code=end


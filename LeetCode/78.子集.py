#
# @lc app=LeetCode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.bc(nums, 0, [])
        return self.res

    def bc(self, nums, start, track):
        self.res.append(track[:])

        for i in range(start, len(nums)):
            track.append(nums[i])
            self.bc(nums, i+1, track)
            track.pop()
# @lc code=end


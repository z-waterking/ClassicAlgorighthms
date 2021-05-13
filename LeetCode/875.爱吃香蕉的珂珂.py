#
# @lc app=LeetCode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#
import math
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.canFinish(piles, mid, h):
                right = mid
            else:
                left = mid + 1
        return left

    def canFinish(self, piles, speed, h):
        time = 0
        for pile in piles:
            time = time + math.ceil(pile/speed)
        return time <= h
# @lc code=end


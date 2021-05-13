#
# @lc app=LeetCode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights) + 1
        while left < right:
            mid = left + (right - left) // 2
            if self.canFinish(weights, mid, D):
                right = mid
            else:
                left = mid + 1
        return left
    def canFinish(self, w, cap, D):
        i = 0
        for day in range(D):
            maxCap = cap
            while maxCap - w[i] >= 0:
                maxCap -= w[i]
                i += 1;
                if i == len(w):
                    return True
        return False
        

# @lc code=end


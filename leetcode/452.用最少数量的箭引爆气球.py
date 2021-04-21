#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        x_end = points[0][1]
        count = 1
        for point in points:
            start = point[0]
            if start > x_end:
                count += 1
                x_end = point[1]
        return count
# @lc code=end


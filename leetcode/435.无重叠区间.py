#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        x_end = intervals[0][1]
        count = 1
        for interval in intervals:
            start = interval[0]
            if start >= x_end:
                count += 1
                x_end = interval[1]

        return len(intervals) - count
# @lc code=end


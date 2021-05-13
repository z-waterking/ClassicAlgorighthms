#
# @lc app=LeetCode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯
        self.res = []
        self.bc(n, k, 1, [])
        return self.res

    def bc(self, n, k, start, track):
        if len(track) == k:
            self.res.append(track[:])
            return

        for i in range(start, n+1):
            track.append(i)
            self.bc(n, k, i+1, track)
            track.pop()
# @lc code=end


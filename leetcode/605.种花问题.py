#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pad_f = [0] + flowerbed + [0]
        count = 0
        for i in range(len(flowerbed)):
            if pad_f[i:i+3] == [0, 0, 0]:
                pad_f[i+1] = 1
                count += 1
        return count >= n

# @lc code=end


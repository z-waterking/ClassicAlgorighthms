#
# @lc app=LeetCode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 正向统计频率
        # 数字:次数
        hs = {}
        for num in nums:
            if num not in hs:
                hs[num] = 1
            else:
                hs[num] += 1

        # 倒排统计
        # 次数:[数字1, 数字2]
        frq = {}
        for i, j in hs.items():
            if j not in frq:
                frq[j] = [i]
            else:
                frq[j].append(i)

        arr = []
        # 找前K个最频繁的
        # 从最后往前开始找，因为最最频繁的出现次数只能是数组长度
        for x in range(len(nums), 0, -1):
            if x in frq:
                arr.extend(frq[x])
        res = [arr[i] for i in range(k)]
        return res
# @lc code=end


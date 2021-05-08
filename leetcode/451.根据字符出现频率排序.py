#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        # 统计出次数
        temp = {}
        for c in s:
            if c not in temp:
                temp[c] = 1
            else:
                temp[c] += 1
        # 倒排
        fq = {}
        for c, f in temp.items():
            if f not in fq:
                fq[f] = [c]
            else:
                fq[f].append(c)

        # 倒序构造
        res = ''
        for f in sorted(fq.keys(), reverse=True):
            for q in fq[f]:
                res += q * f
        return res
# @lc code=end


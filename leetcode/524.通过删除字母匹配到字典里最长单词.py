#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 先对字典排序
        # 1. 长度最长
        # 2. 字典顺序最小
        dictionary.sort(key = lambda x:(-len(x), x))
        
        # 逐个进行判断，字典里的单词不能超出字符串中的
        # 判断方法为：
        # 由于需要顺序相等，因此直接用双指针进行扫描
        for word in dictionary:
            i = 0
            j = 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(word):
                return word

        return ""


# @lc code=end


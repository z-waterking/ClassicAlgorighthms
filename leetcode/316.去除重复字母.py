#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 先统计一下所有字母出现的次数
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        # 利用一个单调栈
        stack = []
        # 判断字母是否存在于栈中
        exist_set = {}

        for c in s:
            # 栈外面的字母先减1
            count[c] -= 1
            # 如果已经在栈中了，跳过
            if exist_set.get(c) == True:
                continue
            
            # 与栈顶的元素比较顺序
            # 弹出栈顶字典序大 & 外面还有的字母
            while len(stack) > 0 and c < stack[-1]:
                # 如果后面没了，就不要删，这次删除停止
                if count[stack[-1]] == 0:
                    break
                exist_set[stack.pop()] = False
                
            # 将未重复的字母加入栈中
            stack.append(c)
            # 标记字符已经存在于栈中了
            exist_set[c] = True
        
        return "".join(stack)
# @lc code=end


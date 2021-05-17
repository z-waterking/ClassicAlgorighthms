#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ''
        # num，N进制转换的方法是：
        # 先求对于N的余数s1,num再除以N
        # ...
        # 求对于N的余数s10，num再除以N
        # 到num为0为止
        # 将s10 ... s1进行排列即可
        if num == 0:
            return '0'

        flag = True
        if num < 0:
            num = -num
            flag = False

        while num != 0:
            res = str(num % 7) + res
            num = num // 7
        
        if flag == False:
            res = '-' + res
            
        return res

# @lc code=end


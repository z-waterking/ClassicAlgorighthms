#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        c=0 #counter
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                c+=1
#               no need to change value at i=0 bcoz we can replace it with any smaller number, so no need to change 
#               but replacing values at other place will violate, thus only handling them
                if i>0:
                    if nums[i-1]<=nums[i+1]:
                        nums[i]=nums[i-1] #useful like when [2,2,3,2,4]
                    else:
                        nums[i+1]=nums[i] #useful like when [2,3,3,2,4]
                # print("after mod",nums)
            if c>1:
                return False
        return True
# @lc code=end


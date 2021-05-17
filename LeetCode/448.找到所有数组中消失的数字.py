#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        res = []

        # 设想一下：如果全都没有重复，即每个字符只出现一次
        # 那么对所有的数字进行一次操作，等于对每个位置进行了一次操作
        # 若有数字重复，例如3重复，则此操作在位置3处会进行两次
        # 即求相反数操作，重复两次，依然为正数
        for num in nums:
            # 应该出现的位置
            pos = abs(num) - 1

            if nums[pos] > 0:
                nums[pos] = -nums[pos]
        
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)

        return res
        

# @lc code=end


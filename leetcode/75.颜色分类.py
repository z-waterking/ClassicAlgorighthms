#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 
        # 0 <-> 红
        # 1 <-> 白
        # 2 <-> 蓝
        # 将0往前放，2往后放
        # 划分为3个区间
        # 0-red: 0  red-blue: 1  blue-结尾: 2
        red, white, blue = 0, 0, len(nums)-1
        # white 是用来进行遍历的，负责将不同的数字往外进行划分
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                # white是从前面过来的，因此不可能漏掉等于0的情况
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                # 这里white还需要再判断一次
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


# @lc code=end


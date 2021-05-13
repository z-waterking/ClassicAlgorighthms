#
# @lc app=LeetCode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 依然需要用二分查找
        # 但是需要知道它是处于前一半还是后一半
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            
            if nums[l] == nums[mid]:
                l += 1
            elif nums[mid] <= nums[r]:
                # 右边排好序
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # 左边排好序
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False
# @lc code=end


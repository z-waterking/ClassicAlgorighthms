# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   BinarySearch.py
@USER       :   ZZZZZ
@TIME       :   2021/4/22 10:21
'''

class BinarySearch():
    '''
    二分查找比较难的地方是如何确定左右边界，以及查找到元素时的左右边界的最终结果。
    此处我将所有的边界全部设置为**闭区间**。只考虑这一种情况即可。
    当然还有另一种情况为左闭右开，不过建议一条道走到黑，只要记住全部闭区间的情况即可。

    查找准确目标是最简单的情形。
    查找左侧边界与右侧边界时，需要进行一点特殊处理。
    '''
    def __init__(self):
        pass

    def SearchTarget(self, nums, target):
        '''
        查找单一目标
        :param nums: 待查找的数组，已经排好序了
        :param target: 查找目标
        :return: 如果找到目标，返回目标索引；否则，返回-1
        '''
        left = 0
        right = len(nums) - 1
        # 都是闭区间，区间结束就是left > right
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # 找到了，直接返回
                return mid
            elif nums[mid] > target:
                # target肯定在左边，缩短右侧边界
                right = mid - 1
            elif nums[mid] < target:
                # target肯定在右边，缩短左侧边界
                left = mid + 1

        # 这里如果能走到，就表示未能查找到
        return -1

    def SearchLeftBound(self, nums, target):
        '''
        nums中存在多个目标，查找最左侧的目标边界
        :param nums: 待查找的数组，已经排好序了
        :param target: 查找目标
        :return:  如果找到目标，返回目标索引；否则，返回-1
        '''
        left = 0
        right = len(nums) - 1

        # 都是闭区间，查找结束就是left > right
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # 找到了，先不急着返回，将区间继续往左移
                right = mid - 1
            elif nums[mid] > target:
                # target肯定在左边，缩短右侧边界
                right = mid - 1
            elif nums[mid] < target:
                # target肯定在右边，缩短左侧边界
                left = mid + 1

        # 最后出来后，这里到底有没有找到呢？
        # 直接检查left是否越界，并检查它指向值
        if left >= len(nums) or nums[left] != target:
            return -1

        return left

    def SearchRightBound(self, nums, target):
        '''
        nums中存在多个目标，查找最左侧的目标边界
        :param nums: 待查找的数组，已经排好序了
        :param target: 查找目标
        :return:  如果找到目标，返回目标索引；否则，返回-1
        '''
        left = 0
        right = len(nums) - 1

        # 都是闭区间，查找结束就是left > right
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                # 找到了，先不急着返回，将区间继续往右移
                left = mid + 1
            elif nums[mid] > target:
                # target肯定在左边，缩短右侧边界
                right = mid - 1
            elif nums[mid] < target:
                # target肯定在右边，缩短左侧边界
                left = mid + 1

        # 最后出来后，这里到底有没有找到呢？
        # 直接检查right是否越界，并检查它指向值
        if right < 0 or nums[right] != target:
            return -1

        return right

if __name__ == "__main__":
    bs = BinarySearch()
    nums = [1, 3, 5, 7, 9, 10, 11]
    # 进行单目标二分查找
    # 能查到的场景
    res = bs.SearchTarget(nums, 7)
    res_left_bound = bs.SearchLeftBound(nums, 7)
    res_right_bound = bs.SearchRightBound(nums, 7)
    print("能查到元素时: {}".format(res))
    print("能查到元素时，左侧边界: {}, 右侧边界: {}".format(res_left_bound, res_right_bound))

    # 查不到的场景
    res = bs.SearchTarget(nums, 0)
    print("查不到到元素时: {}".format(res))

    # 进行左右侧边界的查找
    # 整个目标在最左侧， 最右侧， 中间
    nums1 = [1, 1, 1, 1, 3, 5, 7, 9, 10, 11]
    nums2 = [1, 3, 5, 7, 9, 10, 11, 11, 11, 11]
    nums3 = [1, 3, 4, 7, 7, 7, 7, 9, 10, 11]

    # 对整个目标在最 左 侧进行左右侧边界查找
    res_left_bound = bs.SearchLeftBound(nums1, 1)
    res_right_bound = bs.SearchRightBound(nums1, 1)
    print("当整个目标都在最左侧时，查找结果为: 左边界: {}, 右边界: {}".format(res_left_bound, res_right_bound))

    # 对整个目标在最 右 侧进行左右侧边界查找
    res_left_bound = bs.SearchLeftBound(nums2, 11)
    res_right_bound = bs.SearchRightBound(nums2, 11)
    print("当整个目标都在最右侧时，查找结果为: 左边界: {}, 右边界: {}".format(res_left_bound, res_right_bound))

    # 对整个目标在 中间 时进行左右侧边界查找
    res_left_bound = bs.SearchLeftBound(nums3, 7)
    res_right_bound = bs.SearchRightBound(nums3, 7)
    print("当整个目标都在中间时，查找结果为: 左边界: {}, 右边界: {}".format(res_left_bound, res_right_bound))

    # 左右侧边界查不到的场景
    res_not_found_left = bs.SearchLeftBound(nums1, 0)
    res_not_found_right = bs.SearchRightBound(nums1, 20)
    print("当左右侧边界查找不到时，左侧查找结果: {}, 右侧查找结果: {}".format(res_not_found_left, res_not_found_right))
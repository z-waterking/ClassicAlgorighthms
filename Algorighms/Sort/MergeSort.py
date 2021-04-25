# _*_ coding: utf-8 _*_
"""
@Date:       2021/4/24 4:06 下午
@Author:     wz
@File:       MergeSort.py
@Decs:
"""

class MergeSort:
    # def __init__(self):
    #     pass

    def merge_sort(self, nums):
        '''
        归并排序非递归实现
        Args:
            nums:

        Returns:

        '''

        return nums

    def recursive_merge_sort(self, nums, res, start, end):
        """
        归并排序递归实现
        Args:
            nums:   原list
            res:    每层递归结果存放于辅助list
        Returns:

        """

        if start>=end:
            return

        # 拆分list （下标控制 逻辑拆分）在分布式大规模排序中进行物理拆分
        start1, end1 = start, (start + end) >> 1
        start2, end2 = ((start + end) >> 1) + 1, end

        self.recursive_merge_sort(nums, res, start1, end1)
        self.recursive_merge_sort(nums, res, start2, end2)

        # 合并nums[start1:end1+1]和nums[start2:end2+1]
        k = start
        while start1<=end1 and start2<=end2:
            if nums[start1] <= nums[start2]:
                res[k] = nums[start1]
                start1 += 1
            else:
                res[k] = nums[start2]
                start2 += 1
            k += 1

        while start1<=end1:
            res[k] = nums[start1]
            k += 1
            start1 += 1

        while start2<=end2:
            res[k] = nums[start2]
            k += 1
            start2 += 1

        # 将当前递归层结果从辅助list导回原list，供上层递归层使用
        for i in range(start, end + 1):
            nums[i] = res[i]

    def recursive_merge_sort2(self, nums):
        """
        归并排序递归实现
        Args:
            nums:   原list
            res:    每层递归结果存放于辅助list
        Returns:
        """

        def recursive_merge(nums, start, end):
            '''
            进行递归排序
            :param nums: 待排序数组
            :param start: 开始下标
            :param end: 结束下标
            :return: 排好序的结果
            '''
            # base case, 如果start >= end，则结束
            if start >= end:
                return nums[start:end + 1]

            # 拆分list （下标控制 逻辑拆分）在分布式大规模排序中进行物理拆分
            mid = start + (end - start) // 2
            start1, end1 = start, mid
            start2, end2 = mid + 1, end

            # 对左半边进行排序
            left_res = recursive_merge(nums, start1, end1)
            # 对右半边进行排序
            right_res = recursive_merge(nums, start2, end2)

            # 到这里，左右半边已经排好序了
            # 合并nums[start1:end1+1] 和 nums[start2:end2+1]

            res = [0] * (len(left_res) + len(right_res))
            k = 0
            l = 0
            r = 0
            while l < len(left_res) and r < len(right_res):
                if left_res[l] <= right_res[r]:
                    res[k] = left_res[l]
                    l += 1
                else:
                    res[k] = right_res[r]
                    r += 1
                k += 1

            while l < len(left_res):
                res[k] = left_res[l]
                k += 1
                l += 1

            while r < len(right_res):
                res[k] = right_res[r]
                k += 1
                r += 1

            return res

        return recursive_merge(nums, 0, len(nums) - 1)

if __name__ == "__main__":

    nums = [1,4,7,1,3,7,9,2,0,3]
    res = len(nums) * [0]
    start, end = 0, len(nums) - 1
    sort = MergeSort()

    print("归并排序结果为: {}".format(sort.recursive_merge_sort2(nums)))
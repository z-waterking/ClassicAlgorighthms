# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   BucketSort.py
@USER       :   ZZZZZ
@TIME       :   2021/4/25 11:55
'''

class BucketSort():
    '''
    计数排序:
        对于全为正整数的数组且值处于较小范围内，用计数排序简单直观。
        例：[9, 8, 2, 3, 5, 7, 5, 3, 8]
        只需要申请一个从0到（最大值+1）的数组，将它们建立一一映射。
        初始化桶：[0，0，0，0，0，0，0，0，0，0]
        桶数组编号为0-9，在遍历原数组时，碰到对应的值，则将其索引加一。
        排序后的桶:[0，0，1，2，0，2，0，1，2，1]
        最终，从桶对元素进行还原即可。例如:索引3的值为2，表示有2个3。

    桶排序:
        桶排序则是将最小值到最大值之间每一个固定区域申请空间。
        尽量减少了元素值大小不连续情况下的空间浪费情况。
        将每个元素放入对应的空间（桶）后，桶内进行排序。
        最后再将结果合并，即可完成排序。
    '''
    def __init__(self):
        pass

    def Solution(self, nums):
        '''
        桶排序
        :param nums: 待排序数组
        :return: 排序结果
        '''
        # 先找到对应的最大，最小值
        max_num = max(nums)
        min_num = min(nums)

        # 计算需要的桶的数量,比区间范围多一个
        bucket_num = (max_num - min_num) // (len(nums)) + 1
        # 构建这些桶,初始都为空数组
        buckets = []
        for i in range(bucket_num):
            buckets.append([])

        # 将每个元素放入桶中
        for num in nums:
            # 元素与桶号的映射
            index = int((num - min_num) // len(nums))
            # 将元素加入对应桶
            buckets[index].append(num)

        # 对桶内元素分别进行排序
        for i in range(len(buckets)):
            # 这里应该自己调用其他的排序算法
            # 为了简单，用了python内置的
            buckets[i].sort()

        # 将桶内元素还原
        res = []
        for bucket in buckets:
            res.extend(bucket)

        return res

if __name__ == "__main__":
    bs = BucketSort()
    nums = [4, 5, 2, 9, 1, 2.5, 3.7, 5.9]
    print("桶排序结果为: {}".format(bs.Solution(nums)))

# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   RadixSort.py
@USER       :   ZZZZZ
@TIME       :   2021/4/25 14:03
'''

class RadixSort():
    '''
    基数排序的方式可以采用LSD（Least significant digital）或MSD（Most significant digital
    LSD的排序方式由键值的最右边开始，而MSD则相反，由键值的最左边开始。
    '''
    def __init__(self):
        pass

    def Solution(self, nums):
        '''
        LSD排序方法

        基数排序用正整数比较好。
        分配0-9号桶子，先按照个位数字将这些数放入桶子，再拿出，则可得到个位排好序的数字。
        接着按照十位、百位、千位...亿位（如果有的话），来分配，最后拿出的数组即为排好序的数组。

        问题来了，如何取这些数字的各位呢？
        以 3472 为例，取个位
        个位: (3472 // 1) % 10
        十位：(3472 // 10) % 10
        百位:（3472 // 100) % 10

        到什么时候结束呢？
        * 或者所有的数字取完后全是0
        * 或者到了最高位

        :param nums: 待排序数组
        :return: list，排好序的数组
        '''
        # 初始化
        radix = 1
        # 查询数组中的最大数的位数
        max_num = max(nums)
        max_radix = 0
        while max_num > 0:
            max_radix += 1
            max_num = max_num // 2

        # 阶段的排序结果，后面每次需要用上一次的排序结果来做
        step_res = nums

        while radix <= max_radix:
            buckets = []
            for i in range(10):
                buckets.append([])

            # 对各个数字取其对应的排序基数，放入桶子中
            for num in step_res:
                n = (num // radix) % 10
                buckets[n].append(num)

            step_res = []
            # 从桶里面取出来排序
            for bucket in buckets:
                step_res.extend(bucket)

            # 往上取一个基数
            radix *= 10

        return step_res

if __name__ == "__main__":
    nums = [423, 523, 432, 972, 1]
    rs = RadixSort()
    print("基数排序结果为: {}".format(rs.Solution(nums)))

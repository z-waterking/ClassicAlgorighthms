# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   QuickSort.py
@USER       :   ZZZZZ
@TIME       :   2021/4/21 19:41
'''

class QuickSort():
    '''
        快速排序的性能非常没有保障，对于一些特殊的数组，它不能取得好的性能。
        例如：
            1. 对于基本有序的数组（无论正序还是倒序），它都会做大量无用的切分
            2. 对于重复值较多的数组，会做大量无用切分

        改进：
            1. 尽可能放入随机数组。
            2. 采用三向切分的方法来进行切分，可以避免对重复数据进行反复交换。
                cmp = a[i].compareTo(v)
                if cmp < 0:
                    exch(a, lt++, i++)
                elif cmp > 0:
                    exch(a, i, gt--)
                else:
                    i++
            对应了leetcode75：颜色分类问题。
    '''
    def __init__(self):
        self.exchange_count = 0

    def Solution(self, nums):
        '''
        实现快速排序
        :param nums: 待排序列表
        :return: 排好序的列表
        '''
        def quick_sort(left, right):
            '''
            进行快速排序
            :param nums: 待排序数组
            :param left: 排序的左边界
            :param right: 排序的右边界
            :return: 排好序的数组
            '''
            nonlocal nums
            if left >= right:
                return

            l = left
            r = right

            # 随便找个数
            item = nums[l]

            while l < r:
                # 将右边所有比item小的数字放到左边
                while l < r and nums[r] >= item:
                    r -= 1
                nums[l] = nums[r]

                # 将左边所有比item大的数字放到右边
                while l < r and nums[l] <= item:
                    l += 1
                nums[r] = nums[l]

            # 左边的全比item小，右边的全比item大
            nums[l] = item

            # 分别递归排左边与右边
            quick_sort(left, l)
            quick_sort(l+1, right)

        quick_sort(0, len(nums)-1)
        return nums

    def GetExchangeCount(self):
        return self.exchange_count

if __name__ == "__main__":
    nums = [4, 5, 2, 9, 1]
    st = QuickSort()
    print("快速排序结果为: {}".format(st.Solution(nums)))
    print("交换次数为: {}".format(st.GetExchangeCount()))

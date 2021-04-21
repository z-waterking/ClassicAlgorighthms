# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   BubbleSort.py
@USER       :   ZZZZZ
@TIME       :   2021/4/21 16:41
'''

class BubbleSort():
    def __init__(self):
        self.exchange_count = 0

    def Solution(self, nums):
        '''
        对数组元素进行冒泡排序, 从小到大进行排序
        :param nums: 数字列表
        :return: list, 从小到大排好序的数组
        '''
        # 一共比较 len(nums) - 1 趟即可
        for i in range(len(nums) - 1):
            # 此处每一轮都可以使得最后一个元素就位，因此需要 -i , 不用进行后序的比较了
            for j in range(len(nums) - 1 - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    # 记录一次交换
                    self.exchange_count += 1

        return nums

    def GetExchangeCount(self):
        return self.exchange_count

if __name__ == "__main__":
    nums = [4, 5, 2, 9, 1]
    st = BubbleSort()
    print("冒泡排序结果为: {}".format(st.Solution(nums)))
    print("交换次数为: {}".format(st.GetExchangeCount()))

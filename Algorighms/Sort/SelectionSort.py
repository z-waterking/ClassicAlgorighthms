# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   SelectionSort.py
@USER       :   ZZZZZ
@TIME       :   2021/4/21 17:16
'''

class SelectionSort():
    def __init__(self):
        self.exchange_count = 0

    def Solution(self, nums):
        '''
        对数组元素进行选择排序, 从小到大进行排序
        :param nums: 数字列表
        :return: list, 从小到大排好序的数组
        '''
        # 一共比较 len(nums) - 1 趟即可
        for i in range(len(nums) - 1):
            min_index = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
            self.exchange_count += 1

        return nums

    def GetExchangeCount(self):
        return self.exchange_count

if __name__ == "__main__":
    nums = [4, 5, 2, 9, 1]
    st = SelectionSort()
    print("选择排序结果为: {}".format(st.Solution(nums)))
    print("交换次数为: {}".format(st.GetExchangeCount()))


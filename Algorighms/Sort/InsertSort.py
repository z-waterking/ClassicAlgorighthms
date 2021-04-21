# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   InsertSort.py
@USER       :   ZZZZZ
@TIME       :   2021/4/21 19:25
'''

class InsertSort():
    def __init__(self):
        self.exchange_count = 0

    def Solution(self, nums):
        '''
        对数组元素进行插入排序, 从小到大进行排序
        :param nums: 数字列表
        :return: list, 从小到大排好序的数组
        '''
        # 先假装第一个元素是排好序的，从第二个元素开始，逐个往前面的列表里面插入
        for i in range(len(nums) - 1):
            # 从后往前开始比较
            j = i + 1
            # 保存这个元素
            temp = nums[j]

            while j > 0 and temp < nums[j-1]:
                nums[j] = nums[j - 1]
                j -= 1
                self.exchange_count += 1

            # 找到了位置，把元素放上
            nums[j] = temp

        return nums

    def GetExchangeCount(self):
        return self.exchange_count

if __name__ == "__main__":
    nums = [4, 5, 2, 9, 1]
    st = InsertSort()
    print("插入排序结果为: {}".format(st.Solution(nums)))
    print("交换次数为: {}".format(st.GetExchangeCount()))

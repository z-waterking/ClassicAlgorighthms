# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   ShellSort.py
@USER       :   ZZZZZ
@TIME       :   2021/4/25 13:20
'''

class ShellSort():
    '''
    简单插入排序很循规蹈矩，不管数组分布是怎么样的，依然一步一步的对元素进行比较，移动，插入。
    比如[5,4,3,2,1,0]这种倒序序列，数组末端的0要回到首位置很是费劲，比较和移动元素均需n-1次。
    而希尔排序在数组中采用跳跃式分组的策略，通过某个增量将数组元素划分为若干组，然后分组进行插入排序，随后逐步缩小增量，继续按组进行插入排序操作，直至增量为1。
    希尔排序通过这种策略使得整个数组在初始阶段达到从宏观上看基本有序，小的基本在前，大的基本在后。然后缩小增量，到增量为1时，其实多数情况下只需微调即可，不会涉及过多的数据移动。

　　 我们来看下希尔排序的基本步骤，在此我们选择增量gap=length/2，缩小增量继续以gap = gap/2的方式。
    这种增量选择我们可以用一个序列来表示，{n/2,(n/2)/2...1}，称为增量序列。
    '''
    def __init__(self):
        self.exchange_count = 0

    def Solution(self, nums):
        '''
        对数组元素进行希尔（跨增量的直接插入）排序, 从小到大进行排序
        :param nums: 数字列表
        :return: list, 从小到大排好序的数组
        '''
        gap = len(nums) // 2

        while gap > 0:
            # 先假装第一个元素是排好序的，从第二个元素开始，逐个往前面的列表里面插入
            for i in range(gap, len(nums)):
                # 保存这个元素
                temp = nums[i]
                # 从后往前开始比较
                j = i - gap

                while j >= 0 and temp < nums[j]:
                    nums[j + gap] = nums[j]
                    j -= gap
                    self.exchange_count += 1

                # 找到了位置，把元素放上
                nums[j + gap] = temp

            # 缩小gap
            gap = gap // 2

        return nums

    def GetExchangeCount(self):
        return self.exchange_count

if __name__ == "__main__":
    nums = [4, 5, 2, 9, 1]
    ss = ShellSort()
    print("希尔排序结果为: {}".format(ss.Solution(nums)))
    print("交换次数为: {}".format(ss.GetExchangeCount()))

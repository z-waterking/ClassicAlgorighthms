# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   Permutations.py
@USER       :   ZZZZZ
@TIME       :   2021/5/10 10:33
'''

class Permutations():
    def __init__(self):
        pass

    def permutations(self, nums):
        '''
        求出nums数组中元素的全排列
        :param nums: 待求数组
        :return: 全排列列表
        '''
        self.res = []

        def backtrack(nums, start):
            '''
            求出nums数组所有元素的全排列
            :param nums: 待求组合的数组
            :param start: 数组当前位置开始，之后元素的全排列
            :param track: 暂时记录当前加入组合的元素
            :return: None
            '''
            # 当排列中的数量达到数组的大小时，加入最终结果
            if start == len(nums) - 1:
                self.res.append(nums[:])
                return

            for i in range(start, len(nums)):
                # 选择, 将所有的之后的位置与当前位置进行一次交换
                nums[i], nums[start] = nums[start], nums[i]
                # 回溯
                backtrack(nums, start + 1)
                # 撤销选择，回退交换
                nums[i], nums[start] = nums[start], nums[i]

        backtrack(nums, 0)
        return self.res

if __name__ == "__main__":
    pm = Permutations()
    nums = [2, 7, 1]
    print("数组的全部子集为:{}".format(pm.permutations(nums)))
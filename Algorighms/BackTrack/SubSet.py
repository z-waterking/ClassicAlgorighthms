# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   SubSet.py
@USER       :   ZZZZZ
@TIME       :   2021/5/10 10:23
'''
class SubSet():
    def __init__(self):
        pass

    def subset(self, nums):
        '''
        求出nums数组的全部子集
        :param nums: 待求数组
        :return: 子集列表
        '''
        self.res = []

        def backtrack(nums, start, track):
            '''
            求出nums数组中从start开始的所有子集
            :param nums: 待求子集的数组
            :param start: 数组的开始位置，防止重复求解
            :param track: 暂时记录当前加入子集的元素
            :return:
            '''
            self.res.append(track[:])

            for i in range(start, len(nums)):
                # 选择
                track.append(nums[i])
                # 回溯
                backtrack(nums, i + 1, track)
                # 撤销选择
                track.pop()

        backtrack(nums, 0, [])
        return self.res

if __name__ == "__main__":
    ss = SubSet()
    nums = [2, 7, 1]
    print("数组的全部子集为:{}".format(ss.subset(nums)))

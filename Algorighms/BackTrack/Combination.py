# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   Combination.py
@USER       :   ZZZZZ
@TIME       :   2021/5/10 10:29
'''

class Combination():
    def __init__(self):
        pass

    def combination(self, nums, k):
        '''
        求出包含nums数组k个元素的全部组合
        :param nums: 待求数组
        :return: 组合列表
        '''
        self.res = []

        def backtrack(nums, start, k, track):
            '''
            求出nums数组中从start开始, 后面所有元素中挑出k个元素的组合
            :param nums: 待求组合的数组
            :param start: 数组的开始位置，防止重复求解
            :param k: 组合中需要的元素个数
            :param track: 暂时记录当前加入组合的元素
            :return:
            '''
            # 当组合中的数量达到k时，加入结果集，返回
            if len(track) == k:
                self.res.append(track[:])
                return

            for i in range(start, len(nums)):
                # 选择
                track.append(nums[i])
                # 回溯
                backtrack(nums, i + 1, k, track)
                # 撤销选择
                track.pop()

        backtrack(nums, 0, k, [])
        return self.res

if __name__ == "__main__":
    cb = Combination()
    nums = [2, 7, 1, 5]
    print("数组的全部组合为:{}".format(cb.combination(nums, 3)))


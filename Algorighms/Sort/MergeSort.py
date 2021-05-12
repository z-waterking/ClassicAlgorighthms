# _*_ coding: utf-8 _*_
"""
@Date:       2021/4/24 4:06 下午
@Author:     wz
@File:       MergeSort.py
@Decs:
"""

class MergeSort:
    def __init__(self):
        pass

    def merge_sort(self, nums):
        '''
        归并排序非递归实现
        Args:
            nums: 原list

        Returns: 排好序的数组
        '''
        # 全局res，以进行全局访问原数组
        self.res = nums

        N = len(self.res)
        # 初始归并数组大小为1
        size = 1

        while size < N:
            # 从数组的头开始
            lo = 0
            while lo < N - size:
                # 归并两个大小为size的数组
                self.merge(lo, lo + size - 1, min(lo + size + size - 1, N - 1))
                # 更新下一次归并的头
                lo += size + size
            # 大小为size的子数组已经归并排好序了，继续去归并更大size的数组
            size += size + size

        return self.res

    def recursive_merge_sort(self, nums):
        """
        归并排序递归实现
        Args:
            nums:   原list

        Returns: 排好序的数组
        """
        self.res = nums

        # 递归定义的排序
        def st(lo, hi):
            if hi <= lo:
                return
            mid = lo + (hi - lo) // 2
            st(lo, mid)
            st(mid + 1, hi)
            # 至此，左边与右边均递归排好了序
            # 将排好序的数组进行合并即可
            self.merge(lo, mid, hi)

        st(0, len(self.res) - 1)
        return self.res

    def merge(self, lo, mid, hi):
        '''
        将数组中self.res[lo:mid]和self.res[mid:hi]进行归并
        :param lo: 数组的下界
        :param mid: 数组的中位索引
        :param hi: 数组的上界
        :return:
        '''
        i = lo
        j = mid + 1

        # 辅助数组,暂时保存了当前所有的元素
        aux = self.res[:]
        # 将辅助数组中的值逐个放回原数组
        for k in range(lo, hi + 1):
            # 此时，前半个数组已经空了，将后半个数组元素加入即可
            if i > mid:
                self.res[k] = aux[j]
                j += 1
            # 此时，后半个数组已经空了，将前半个数组元素加入即可
            elif j > hi:
                self.res[k] = aux[i]
                i += 1
            # 判断aux[i]和aux[j]的大小，将较小的那个放入数组
            elif aux[i] < aux[j]:
                self.res[k] = aux[i]
                i += 1
            else:
                self.res[k] = aux[j]
                j += 1

if __name__ == "__main__":
    nums = [1,4,7,1,3,7,9,2,0,3]
    ms = MergeSort()

    print("递归-归并排序结果为: {}".format(ms.recursive_merge_sort(nums)))
    print("非递归-归并排序结果为: {}".format(ms.merge_sort(nums)))
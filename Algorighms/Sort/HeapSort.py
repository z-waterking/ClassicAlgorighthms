# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   HeapSort.py
@USER       :   ZZZZZ
@TIME       :   2021/4/25 12:51
'''


class HeapSort():
    '''
    堆排序: 由小到大
    堆排序要对输入的数组构造一个堆，
    '''
    def __init__(self):
        # 最前面插入一个元素，使得索引i的左子结点为2i，右子结点为2i+1
        self.__heap = [-1]
        self.__heap_length = 0

# ---------------------------- 公有方法 ----------------------------
    def Solution(self, nums):
        '''
        通过数组构造一个堆，进行堆排序，返回结果
        :param nums: 构造堆的数组
        :return: 排序结果
        '''
        # 将所有元素先加入堆
        self.__heap.extend(nums)
        self.__heap_length += len(nums)
        # 构造堆
        self._heapify()
        # 进行排序
        res = []
        while self.empty() == False:
            res.append(self.pop())
        # 返回结果
        return res

    def pop(self):
        '''
        取出堆顶元素
        :return: 堆顶元素
        '''
        if self.empty() == True:
            raise Exception("empty heap!")

        # 最后一个元素放到堆顶位置
        self.__heap[1], self.__heap[-1] = self.__heap[-1], self.__heap[1]

        # 取出最后一个元素
        res = self.__heap.pop()
        self.__heap_length -= 1
        # 对堆顶进行下沉
        self._sift_down(1)

        return res

    def empty(self):
        '''
        判断堆是否是空的
        :return: True if the heap is empty else False
        '''
        if self.__heap_length == 0:
            return True
        else:
            return False

# ---------------------------- 私有方法 ----------------------------
    def _heapify(self):
        '''
        将数组变成一个堆
        :return: None
        '''
        # 从第一个非叶子结点开始进行操作
        index = self.__heap_length // 2
        while index >= 1:
            self._sift_down(index)
            index -= 1

    def _sift_up(self, index):
        '''
        将index结点上浮
        :param index: 上浮的结点索引
        :return: None
        '''
        # 当父节点到0时，不必再向上了
        while index // 2 > 0 and self.__heap[index] < self.__heap[index // 2]:
            self.__heap[index], self.__heap[index // 2] = self.__heap[index // 2], self.__heap[index]
            index = index // 2

    def _sift_down(self, index):
        '''
        将index结点下沉
        :param index: 下沉的结点索引
        :return: None
        '''
        # 当左结点没有值时，就不必探索了
        while 2 * index <= self.__heap_length:

            # 比较左右结点的值
            min_index = 2 * index
            if min_index + 1 <= self.__heap_length and self.__heap[min_index + 1] < self.__heap[min_index]:
                min_index = min_index + 1

            # 如果根结点大，则交换当前结点与左右结点中较小的那个
            if self.__heap[index] > self.__heap[min_index]:
                # 继续向下探索
                self.__heap[index], self.__heap[min_index] = self.__heap[min_index], self.__heap[index]
                index = min_index
            else:
                break

if __name__ == "__main__":
    #构造一个堆
    hs = HeapSort()
    res = hs.Solution([18, 14, 17, 8, 15, 12, 11, 1, 7, 6, 9])
    print("堆排序的结果为: {}".format(res))
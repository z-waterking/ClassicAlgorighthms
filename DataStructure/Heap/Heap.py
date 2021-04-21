# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   Heap.py
@USER       :   ZZZZZ
@TIME       :   2021/4/21 23:36
'''
import logging
logging.basicConfig(level = logging.INFO)

class Heap():
    '''
    实现一个最大堆
    '''
    def __init__(self):
        # 最前面插入一个元素，使得索引i的左子结点为2i，右子结点为2i+1
        self.__heap = [-1]
        self.__heap_length = 0

# ---------------------------- 公有方法 ----------------------------
    def init(self, nums):
        '''
        通过数组构造一个堆
        :param nums: 构造堆的数组
        :return: None
        '''
        if type(nums) != list:
            raise Exception("please offer a list!")
        # 清空堆
        self.clear()
        # 将所有元素先加入堆
        self.__heap.extend(nums)
        self.__heap_length += len(nums)
        # 构造堆
        self._heapify()

    def push(self, value):
        '''
        向堆中插入一个元素
        :param value: 插入的元素值
        :return: None
        '''
        # 直接将元素插入最后，向上调整
        self.__heap.append(value)
        self.__heap_length += 1

        # 向上调整
        self._shift_up(self.__heap_length)

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
        self._shift_down(1)

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

    def clear(self):
        '''
        清空堆中的元素
        :return: None
        '''
        logging.info("clear heap!")
        self.__init__()

# ---------------------------- 私有方法 ----------------------------
    def _heapify(self):
        '''
        将数组变成一个堆
        :return: None
        '''
        # 从第一个非叶子结点开始进行操作
        index = self.__heap_length // 2
        while index >= 1:
            self._shift_down(index)
            index -= 1

    def _shift_up(self, index):
        '''
        将index结点上浮
        :param index: 上浮的结点索引
        :return: None
        '''
        while index // 2 > 0 and self.__heap[index] > self.__heap[index // 2]:
            self.__heap[index], self.__heap[index // 2] = self.__heap[index // 2], self.__heap[index]
            index = index // 2

    def _shift_down(self, index):
        '''
        将index结点下沉
        :param index: 下沉的结点索引
        :return: None
        '''
        # 当左结点没有值时，就不必探索了
        while 2 * index <= self.__heap_length:

            # 比较左右结点的值
            max_index = 2 * index
            if max_index + 1 < self.__heap_length and self.__heap[max_index + 1] > self.__heap[max_index]:
                max_index = max_index + 1

            # 如果根结点小，则交换当前结点与左右结点中较大的那个
            if self.__heap[index] < self.__heap[max_index]:
                # 继续向下探索
                self.__heap[index], self.__heap[max_index] = self.__heap[max_index], self.__heap[index]
                index = max_index
            else:
                break

# ---------------------------- 内部方法 ----------------------------
    def __str__(self):
        res_heap = [str(item) for item in self.__heap]
        res = "共{}个元素: ".format(self.__heap_length) + ",".join(res_heap[1:])
        return res

if __name__ == "__main__":
    #构造一个堆
    hp = Heap()
    hp.init([18, 14, 17, 8, 15, 12, 11, 1, 7, 6, 9])
    print("最大堆的初始化: {}".format(hp))

    # 插入一个中间元素
    hp.push(13)
    print("插入中间元素后: {}".format(hp))

    # 插入一个最大元素
    hp.push(20)
    print("插入最大元素后: {}".format(hp))

    # 取出堆顶元素
    res = hp.pop()
    print("堆顶元素为: {}".format(res))
    print("取出堆顶元素后: {}".format(hp))

    # 进行堆排序
    print("堆排序的结果为:")
    res = []
    while hp.empty() == False:
        res.append(hp.pop())
    print(res)

    # 堆排序后的结果
    print("堆排序后的结果为: {}".format(hp))
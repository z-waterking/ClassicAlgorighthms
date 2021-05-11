# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   MinStack.py
@USER       :   ZZZZZ
@TIME       :   2021/4/21 20:06
'''
import math
import logging
logging.basicConfig(level = logging.INFO)

class MinStack():
    def __init__(self):
        # 常规栈
        self.__stack = []
        self.__stack_length = 0
        # 辅助最小栈
        self.__min_stack = []
        self.__min_stack_length = 0

# ---------------------------- 公有方法 ----------------------------
    def init(self, val_list):
        '''
        将所有的val值加入栈
        :param val_list: 入栈参数
        :return: None
        '''
        self.clear()

        for value in val_list:
            self.push(value)
        logging.info("init success!")

    def push(self, value):
        '''
        将元素压入栈
        :param value: 待压入的元素值
        :return: None
        '''
        if math.isnan(value):
            raise Exception("not a number!")

        self.__stack.append(value)
        self.__stack_length += 1

        # 如果最小栈为空，则直接放入
        if len(self.__min_stack) == 0:
            self.__min_stack.append(value)
            self.__min_stack_length += 1
        else:
            # 否则，只有比栈顶元素小时，才加入
            if value < self.__min_stack[-1]:
                self.__min_stack.append(value)
                self.__min_stack_length += 1

    def pop(self):
        '''
        从最小栈中弹出元素
        :return: 弹出的元素
        '''
        if self.__min_stack_length == 0:
            raise Exception("stack has been empty!")
        # 主栈中的直接出栈
        value = self.__stack.pop()
        self.__stack_length -= 1

        # 若值与最小栈中的相等，则最小栈也出栈
        if value == self.__min_stack[-1]:
            self.__min_stack.pop()
            self.__min_stack_length -= 1
        return value

    def GetMin(self):
        '''
        取得最小元素
        :return: 最小值
        '''
        if self.__min_stack_length == 0:
            raise Exception("no elements!")
        return self.__min_stack[-1]

    def clear(self):
        '''
        清空栈
        :return: None
        '''
        logging.info("clear stack!")
        self.__init__()

# ---------------------------- 内部方法 ----------------------------
    def __str__(self):
        stack_res = ",".join([str(item) for item in self.__stack])
        min_stack_res = ",".join([str(item) for item in self.__min_stack])
        res = "主栈: {}\n最小栈: {}".format(stack_res, min_stack_res)
        return res

if __name__ == "__main__":
    # 初始化最小栈
    ms = MinStack()
    ms.init([3, 8, 5, 6, 9, 1, 0])
    print("初始化后的栈:\n{}".format(ms))

    # 插入一个非最小元素
    ms.push(8)
    print("插入非最小元素后的栈:\n{}".format(ms))

    # 删除一个非最小元素
    ms.pop()
    print("删除非最小元素后的栈:\n{}".format(ms))

    # 删除最小元素的栈
    ms.pop()
    print("删除最小元素后的栈:\n{}".format(ms))

    # 取得最小元素
    print("当前的最小元素为: {}".format(ms.GetMin()))

    # 清空栈
    ms.clear()
    print("清空后的栈:\n{}".format(ms))

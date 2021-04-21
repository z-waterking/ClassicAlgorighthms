# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   单链表.py
@USER       :   ZZZZZ
@TIME       :   2021/4/21 13:51
'''
import logging
logging.basicConfig(level = logging.INFO)

# 单链表结点
class Node(object):

    def __init__(self, val = "", next = None):
        self.val = val
        self.next = next


# 单链表
class SingleLinkedList():
    '''
        由于构造了头结点，因此在插入与删除时，不需要对空链表进行单独考虑。
    '''

    def __init__(self):
        # 带头结点的单链表
        self.__head = Node(val = "head")
        self.__length = 0

    def init(self, val_list):
        '''
        从传入的列表中构造单链表
        :param val_list: 一个列表，顺序列出需要构造的元素
        :return: None
        '''
        if type(val_list) != list:
            raise Exception("Please offer a list!")

        # 按顺序构造链表
        temp_pointer = self.__head
        for val in val_list:
            temp_pointer.next = Node(val = val)
            temp_pointer = temp_pointer.next

        self.__length = len(val_list)

    def head_add(self, value):
        '''
        头部增加一个元素
        :param value: 元素值
        :return: None
        '''
        node = Node(val = value)
        node.next = self.__head
        self.__head.next = node

        self.__length += 1

    def tail_add(self, value):
        '''
        尾部增加一个元素
        :param value: 元素值
        :return: None
        '''
        node = self.__head
        while node.next != None:
            node = node.next

        node.next = Node(val = value)

        self.__length += 1

    def insert(self, index, value):
        '''
        向列表中间插入元素
        :param index: 插入元素的位置，1，2，3，..., self.__length
        :param value: 插入元素的值
        :return: None
        '''
        if index > self.__length or index < 0:
            raise Exception("index invalid!")

        node = self.__head
        # 得到此位置的前一个结点
        for i in range(index - 1):
            node = node.next

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

    def delete(self, index):
        '''
        从链表中删除元素
        :param index: 删除元素的位置
        :return: None
        '''
        if index > self.__length or index < 0:
            raise Exception("index invalid!")

        node = self.__head
        # 得到此位置的前一个结点
        for i in range(index - 1):
            node = node.next

        node.next = node.next.next

    def __str__(self):
        '''
        print(SingleLinkedList())
        :return: str includes all vals
        '''
        res = []
        node = self.__head.next
        while node != None:
            res.append(str(node.val))
            node = node.next
        return ",".join(res)

if __name__ == "__main__":
    sl = SingleLinkedList()
    sl.init([1, 2, 3])
    print(sl)

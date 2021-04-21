# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   SingleLinkedList.py
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

# ---------------------------- 公有方法 ----------------------------
    def init(self, val_list):
        '''
        从传入的列表中构造单链表
        :param val_list: 一个列表，顺序列出需要构造的元素
        :return: None
        '''
        if type(val_list) != list:
            raise Exception("Please offer a list!")

        self.clear()

        # 按顺序构造链表
        temp_pointer = self.__head
        for val in val_list:
            temp_pointer.next = Node(val = val)
            temp_pointer = temp_pointer.next

        self._reset_len()
        self._add_len(len(val_list))

    def head_insert(self, value):
        '''
        头部增加一个元素
        :param value: 元素值
        :return: None
        '''
        node = Node(val = value)
        node.next = self.__head.next
        self.__head.next = node

        self._add_len(1)

    def tail_insert(self, value):
        '''
        尾部增加一个元素
        :param value: 元素值
        :return: None
        '''
        node = self.__head
        while node.next != None:
            node = node.next

        node.next = Node(val = value)

        self._add_len(1)

    def index_insert(self, index, value):
        '''
        向列表中间插入元素
        :param index: 插入元素的位置，1，2，3，..., self.__length, sele.__length+1
        :param value: 插入元素的值
        :return: None
        '''
        if index > self.__length + 1 or index < 0:
            raise Exception("index invalid!")

        node = self.__head
        # 得到此位置的前一个结点
        for i in range(index - 1):
            node = node.next

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

        self._add_len(1)

    def head_delete(self):
        '''
        从头部删除元素
        :return:
        '''
        if self.__length == 0:
            raise Exception("empty list!")

        self.__head.next = self.__head.next.next
        self._sub_len(1)

    def tail_delete(self):
        '''
        从尾部删除元素
        :return:
        '''
        if self.__length == 0:
            raise Exception("empty list!")

        # 走到倒数第二个结点
        node = self.__head
        while node.next.next != None:
            node = node.next

        node.next = node.next.next
        self._sub_len(1)

    def index_delete(self, index):
        '''
        从链表中删除某位置元素
        :param index: 删除元素的位置
        :return: None
        '''
        if index > self.__length or index < 0:
            raise Exception("index invalid!")

        if self.__length == 0:
            raise Exception("empty list!")

        node = self.__head
        # 得到此位置的前一个结点
        for i in range(index - 1):
            node = node.next

        node.next = node.next.next
        self._sub_len(1)

    def reverse(self):
        '''
        反转整个链表
        :return:
        '''
        def reverse_recursion(head):
            '''
            递归反转以head为头的链表
            :param node:
            :return:
            '''
            if head == None or head.next == None:
                return head

            # 递归下去，返回新的头结点
            new_head = reverse_recursion(head.next)

            # 之前的head与递归后的尾部相连，手动将其反转
            head.next.next = head
            head.next = None

            return new_head

        # 递归反转链表
        self.__head.next = reverse_recursion(self.__head.next)

    def clear(self):
        '''
        清空单链表
        :return:
        '''
        logging.info("clear LinkedList!")
        self.__init__()

#---------------------------- 私有方法 ----------------------------
    def _reset_len(self):
        self.__length = 0

    def _add_len(self, num = 1):
        self.__length += num

    def _sub_len(self, num = 1):
        self.__length -= num

#---------------------------- 内部方法 ----------------------------
    def __len__(self):
        '''
        获得单链表的长度
        :return: lenght of LinkedList
        '''
        return self.__length

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

#---------------------------- 测试代码 ----------------------------
if __name__ == "__main__":
    sl = SingleLinkedList()
    # 初始化代码
    sl.init([1, 2, 3])
    print('初始化后: {}'.format(str(sl)))

    sl.head_insert(5)
    print('头插后: {}'.format(str(sl)))

    sl.tail_delete()
    print('尾删后: {}'.format(str(sl)))

    sl.index_insert(2, 3)
    print('索引插入后:(2, 3) : {}'.format(str(sl)))

    sl.index_delete(4)
    print('索引删除后: 4 : {}'.format(str(sl)))

    sl.reverse()
    print('反转后: {}'.format(str(sl)))

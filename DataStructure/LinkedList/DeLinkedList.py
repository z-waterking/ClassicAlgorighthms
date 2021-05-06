# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   DeLinkedList.py
@USER       :   ZZZZZ
@TIME       :   2021/4/22 23:45
'''
import logging
logging.basicConfig(level = logging.INFO)

# 双向链表结点
class DeNode(object):

    def __init__(self, val = "", left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 双向链表
class DeLinkedList():
    '''
        由于构造了头结点与尾结点，因此在插入与删除时，不需要对空链表进行单独考虑。
        对于插入操作，遵循以下顺序：
        1. 先操作新构造的结点，将其左右结点放好
        2. 再操作原头/尾结点，操作时要保持通过头/尾结点能找到相邻结点
    '''

    def __init__(self):
        # 带头结点与尾结点的双向链表
        self.__head = DeNode(val = "head")
        self.__tail = DeNode(val = "tail")
        # 将头结点与尾结点相连
        self.__head.right = self.__tail
        self.__tail.left = self.__head

        self.__length = 0

# ---------------------------- 公有方法 ----------------------------
    def init(self, val_list):
        '''
        从传入的列表中构造双向链表
        :param val_list: 一个列表，顺序列出需要构造的元素
        :return: None
        '''
        if type(val_list) != list:
            raise Exception("Please offer a list!")

        self.clear()

        # 按从左到右的顺序构造链表,即尾插操作
        for val in val_list:
            # 由于存在尾结点，因此直接调用自己的尾插方法
            self.tail_insert(val)

        # 更新元素数量
        self._reset_len()
        self._add_len(len(val_list))

    def head_insert(self, value):
        '''
        头部增加一个元素
        :param value: 元素值
        :return: None
        '''
        new_node = DeNode(val = value)
        # 1. 新结点的 左边 与头结点相连
        new_node.left = self.__head
        # 2. 新结点的 右边 与头结点的 右边 相连
        new_node.right = self.__head.right
        # 3. 原初始结点的 左边 与新结点相连
        self.__head.right.left = new_node
        # 4. 头结点的右边与新结点相连
        self.__head.right = new_node

        self._add_len(1)

    def tail_insert(self, value):
        '''
        尾部增加一个元素
        :param value: 元素值
        :return: None
        '''
        # 新建一个结点
        new_node = DeNode(val = value)
        # 双向链表这里需要分四步
        # 1. 新结点的 左边 与尾结点的 左边 相连
        new_node.left = self.__tail.left
        # 2. 新结点的 右边 与尾结点相连
        new_node.right = self.__tail
        # 3. 原最后一个结点的 右边 与新结点相连
        self.__tail.left.right = new_node
        # 4. 尾结点的 左边 与新结点相连
        self.__tail.left = new_node

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
            node = node.right

        new_node = DeNode(val=value)
        # 1. 新结点的 左边 与相应结点相连
        new_node.left = node
        # 2. 新结点的 右边 与相应结点的 右边 相连
        new_node.right = node.right
        # 3. 相应结点的右边结点的 左边 与新结点相连
        node.right.left = new_node
        # 4. 相应结点的右边与新结点相连
        node.right = new_node

        self._add_len(1)

    def head_delete(self):
        '''
        从头部删除元素
        :return:
        '''
        if self.__length == 0:
            raise Exception("empty list!")

        # 1. 找到删除后的下一个结点
        new_node = self.__head.right.right
        # 2. 将头部元素的 右边 与对应结点相连
        self.__head.right = new_node
        # 3. 将头部元素的 下一个的下一个 的 左边 与头元素相连
        new_node.left = self.__head

        self._sub_len(1)

    def tail_delete(self):
        '''
        从尾部删除元素
        :return:
        '''
        if self.__length == 0:
            raise Exception("empty list!")

        # 1. 找到删除后的上一个结点
        new_node = self.__tail.left.left
        # 2. 将尾部元素的 左边 与对应结点相连
        self.__tail.left = new_node
        # 3. 将尾部元素的 上一个的上一个 的 右边 与尾元素相连
        new_node.right = self.__tail

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
            node = node.right

        # 1. 找到删除后的下一个结点
        new_node = node.right.right
        # 2. 将下一个结点的左边与此结点相连
        new_node.left = node
        # 3. 将此结点的右边与下一个结点相连
        node.right = new_node

        self._sub_len(1)

    def search(self, value):
        '''
        查找某个元素是否存在
        :param value: 待查找的元素值
        :return: 如果元素存在，True; 否则，False
        '''
        node = self.__head.right
        # 顺序遍历链表
        while node != None:
            # 挨个比较元素值
            if node.val == value:
                return True
            node = node.right

        # 如果走到了这里，已经没查到
        return False

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
        node = self.__head.right
        while node != self.__tail:
            res.append(str(node.val))
            node = node.right
        return "<->".join(res)

#---------------------------- 测试代码 ----------------------------
if __name__ == "__main__":
    dl = DeLinkedList()
    # 初始化代码
    dl.init([1, 2, 3])
    print('初始化后: {}'.format(str(dl)))

    dl.head_insert(5)
    print('头插后: {}'.format(str(dl)))

    dl.tail_delete()
    print('尾删后: {}'.format(str(dl)))

    dl.index_insert(2, 3)
    print('索引插入后:(2, 3) : {}'.format(str(dl)))

    dl.index_delete(4)
    print('索引删除后: 4 : {}'.format(str(dl)))

    res = dl.search(5)
    print('查找存在的元素: 5 : {}'.format(res))

    res = dl.search(2)
    print('查找不存在的元素: 2 : {}'.format(res))

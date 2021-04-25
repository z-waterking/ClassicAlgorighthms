# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   HashTable.py
@USER       :   ZZZZZ
@TIME       :   2021/4/25 18:25
'''
class Node():
    '''
    链地址法解决冲突的结点
    '''
    def __init__(self, value = None, next = None):
        self.val = value
        self.next = next

class HashTable():
    '''
    哈希表是根据 值 直接进行访问的数据结构。
    具体来说，通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。
    这个映射函数叫做 散列函数，存放记录的数组叫做 散列表。

    其中有两个关键点：
    1. 如何把值映射到一个位置？
        (1) * 除余法: h（k) = k mod p
        (2) 平方散列法: h(k) = (value^2) >> 28
        (3) 斐波那契散列法: h(k) = (value * 2654435769(MAX_INT32) ) >> 28
    2. 如果两个值映射到了同一个位置，该怎么办？
        (1) 开放定址法：线性重散列 二次重散列
        (2) * 链地址法：每个地址作为一个链来存储
        (3) 再散列法：构造多个hash函数

    Notice:
        想想，如果在链地址法中，将每个表结点作为一颗平衡二叉树的根结点，那么每个位置都将成为一棵平衡二叉树
        查找时间复杂度变成了log2N，并且由于经过了哈希，分散了结点数量，真实运行起来会更快一些

    本例中用除余法取哈希值
    用链地址法解决冲突
    '''
    def __init__(self):
        # 哈希表的大小
        self._table_size = 11
        # 哈希表，每个元素是个表头，采用头插法放入元素
        self._table = []
        for i in range(self._table_size):
            self._table.append(Node())

        # 元素个数
        self._count = 0

    def init(self, values):
        '''
        通过一个列表构造哈希表
        :param values: 待构造的列表
        :return: None
        '''
        for value in values:
            self.insert(value)

    def insert(self, value):
        '''
        向哈希表中插入一个值
        :param value: 待插入值
        :return: None
        '''
        # 找到了它的位置
        index = self._hash(value)
        # 为这个值建立结点
        node = Node(value = value)
        # 头插法插入对应的位置
        node.next = self._table[index].next
        self._table[index].next = node
        # 数量+1
        self._count += 1

    def delete(self, value):
        '''
        从哈希表中删除一个值
        :param value: 待删除值
        :return: None
        '''
        # 找到它的哈希位置
        index = self._hash(value)
        # 在链表中进行查询
        pre_node = self._table[index]
        node = self._table[index].next
        if self.search(value) == False:
            raise Exception("no this value!")

        # 注意，这里按照链表的构造，只要查到这个值，是可以通过将它的下一个值赋给它，将下一个结点删掉的操作来进行的。
        # 但是可能查到的这个值就是最后一个结点，那么上述方法行不通。
        while node != None:
            # 找到值了，停下来
            if node.val == value:
                break
            else:
                pre_node = pre_node.next
                node = node.next

        # 把node删除
        pre_node.next = node.next

    def search(self, value):
        '''
        从哈希表中查找一个值
        :param value: 待查找的值
        :return: 如果找到这个值，返回True；否则，返回False
        '''
        # 找到它的哈希位置
        index = self._hash(value)
        # 在链表中进行查询
        node = self._table[index]
        while node != None:
            if node.val == value:
                return True
            node = node.next

        # 如果走到这，肯定就没查找
        return False


# ---------------------------- 私有方法 ----------------------------
    def _hash(self, value):
        '''
        哈希函数，通过给定的值，计算出一个位置
        :param value: 存入哈希表的值
        :return: 散列表中的位置
        '''
        return value % self._table_size

# ---------------------------- 内部方法 ----------------------------
    def __str__(self):
        final_res = ""
        for i in range(self._table_size):
            res = []
            node = self._table[i].next
            while node != None:
                res.append(str(node.val))
                node = node.next

            final_res += "索引为{}的位置的值为: {}\n".format(i, ",".join(res))

        return final_res

if __name__ == "__main__":
    ht = HashTable()

    # 初始化
    ht.init([2, 3, 5, 8, 9, 10, 2, 9, 1, 5, 2, 1, 7, 9, 11])
    print("初始化后的哈希表为:\n{}".format(ht))

    # 插入结点
    ht.insert(9)
    print("插入值后的哈希表为:\n{}".format(ht))

    # 删除结点
    ht.delete(11)
    print("删除值后的哈希表为:\n{}".format(ht))

    # 查找结点
    res = ht.search(8)
    print("查找值为8的结果为: {}".format(res))


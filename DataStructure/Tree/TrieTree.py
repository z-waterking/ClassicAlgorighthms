# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   TrieTree.py
@USER       :   ZZZZZ
@TIME       :   2021/4/22 14:21
'''
class TrieNode():
    '''
    实现一个可以指向26个小写字母的树结点
    顺便要进行自我管理
    '''
    def __init__(self):
        '''
        字典树结点的初始化
        count 来表示以此结点结尾的单词数量
        pointers 来表示此结点指向的下游结点
        '''
        self.count = 0
        self.pointers = [None] * 26
        self._traverse_dict = {}

    def isLeafNode(self):
        '''
        判断是否是叶子结点
        :return: True 如果后面没有结点了；否则 False
        '''
        if self.pointers.count(None) == 26:
            return True
        else:
            return False

class TrieTree():
    '''
    a-z字典树，用0-25索引来表示
    Notice: 字典树的核心并不在于结点，而在于其结构。其 **结构** 存储了一个字符串的信息。
    最后的结点记录了这个串出现了几次
    '''
    def __init__(self):
        self.__root = TrieNode()
        self.__count = 0

# ---------------------------- 公有方法 ----------------------------
    def init(self, strings_list):
        '''
        通过strings_list构造一颗字典树
        :param strings_list: 传入的strings列表
        :return: None
        '''
        # 调用自己内部的方法，将一列串加进去
        for string in strings_list:
            self.add_string(string)

    def add_string(self, string):
        '''
        增加一个串
        :param string: 待增加的串
        :return: None
        '''
        node = self.__root
        # 对每一个字符，从根节点开始
        for c in string:
            # 找到它的索引
            index = self._char_to_num(c)
            # 这个索引指向不存在时，对应的索引建立结点
            if node.pointers[index] == None:
                node.pointers[index] = TrieNode()
            # node向下走一步
            node = node.pointers[index]
        # 走到最后之后，将node里面的count + 1，表示这里是一个串的结束
        node.count += 1
        self.__count += 1

    def search_string(self, string):
        '''
        查找字典树中是否存在串
        :param string: 待查找的string
        :return: 若存在，返回True；若不存在，返回False
        '''
        node = self.__root
        for c in string:
            # 找到对应的索引
            index = self._char_to_num(c)
            # 如果是个None，则表明不存在
            if node.pointers[index] == None:
                return False
            node = node.pointers[index]
        # 走到头之后，看看它的count是不是0
        # 如果是0， 则表明不存在
        if node.count == 0:
            return False
        else:
            return True

    def auto_complete(self, prefix):
        '''
        查找与prefix具有相同前缀的串
        :param prefix: 前缀
        :return: list，所有与prefix相同的列表
        '''
        # 先走到这个前缀树的最后一个位置
        # 例如去查前缀为aa的，则先走过aa。
        # 将当前结点当作根节点，prefix作为初始字符串，对接下去的树进行先序遍历
        self._traverse_dict = {}
        node = self.__root
        for c in prefix:
            # 如果中间走到了None，则表明不存在此前缀
            if node == None:
                return []
            index = self._char_to_num(c)
            node = node.pointers[index]

        # 采用先序递归遍历进行遍历
        self._traverse(node, prefix)
        return list(self._traverse_dict.keys())

    def delete_string(self, string):
        '''
        删除字典树中的串:
        这是一个比较困难的操作。
        在删除时，可能碰到以下场景：
        1. 要删除的串是其他串的前缀，例如abcde,abc里面将abc删除，则只需要将对应位置的count变为0，即可返回
        2. 要删除的串是其他串的后缀，（单独存在的串可视作空串''的后缀），例如abc,abcde里面要删除abcde，则需要逐步回溯，将上游结点也删掉
        :param string: 待删除的串
        :return: None
        '''
        # 如果能找得到，才进行删除
        if self.search_string(string) == False:
            raise Exception("please offer a valid string!")

        # 采用递归遍历的形式;当然，也可以自己采用栈的形式。
        # 当你作为一个结点时，考虑子节点的返回
        def delele(node, string, depth):
            # base case
            if node == None:
                return node

            # 如果已经找到了对应的结点了
            if depth == len(string):
                # 处理树中的串数量
                self.__count -= node.count
                # 将对应结点的置为0
                node.count = 0
            else:
                # 找到当前的字符
                c = string[depth]
                index = self._char_to_num(c)
                # 往下递归一层
                node.pointers[index] = delele(node.pointers[index], string, depth + 1)

            # 假装：现在已经把node的所有子结点处理完，递归回来了，node该怎么办？
            # 主要问题在于node需要保留吗？
            # 在它还有子结点或者本身是另外一个结点的结束(count不为0)时，需要保留
            if node.count != 0 or node.isLeafNode() == False:
                return node
            else:
                return None

        delele(self.__root, string, 0)
        # 如果把root删了，则恢复一下
        if self.__root == None:
            self.__root = TrieNode()

    def GetStringCount(self):
        '''
        获取字典树中的串的数量
        :return: 字典树中的串的数量
        '''
        return self.__count

    def clear(self):
        '''
        清空所有元素
        :return: None
        '''
        self.__init__()

# ---------------------------- 私有方法 ----------------------------
    def _char_to_num(self, char):
        '''
        将小写字母转为0-25
        :param char: 待转换的小写字母
        :return: 小写字母的序号
        '''
        return ord(char) - ord('a')

    def _num_to_char(self, num):
        '''
        将0-25转换为小写字母
        :param num: 待转换的数组
        :return: 小写字母
        '''
        return chr(ord('a') + num)

    # 先序递归遍历整个字典树的方法
    def _traverse(self, node, one_res):
        '''
        遍历以node为结点的整个字典树，将遍历结果记入self._traverse_dict
        :param node: 树的起始结点
        :param one_res: 遇到的一个终点
        :return: None
        '''
        if node == None:
            return

        # 如果找到了，则将这个加进去
        if node.count != 0:
            self._traverse_dict[one_res] = node.count

        # 进行递归遍历
        for i in range(len(node.pointers)):
            # 将这个字符加在串上，继续往下遍历
            c = self._num_to_char(i)
            self._traverse(node.pointers[i], one_res + c)

# ---------------------------- 内部方法 ----------------------------
    def __str__(self):
        # 遍历一下所有的串，返回一个字典，标识里面存在的串与个数
        self._traverse_dict = {}
        self._traverse(self.__root, '')
        return "共有{}个元素: ".format(self.__count) + str(self._traverse_dict)

if __name__ == "__main__":
    tt = TrieTree()
    # 初始化字典树
    tt.init(["aaaaaa", "abcde", "abcdef", "abc", "print", "aaa", "aaa"])
    print("初始化后的字典树为:\n{}".format(tt))

    # 增加一个不存在的元素
    tt.add_string("zxy")
    print("增加不存在的元素: zxy 后为:\n{}".format(tt))

    # 增加一个已存在的元素
    tt.add_string("abcde")
    print("增加已存在的元素: abcde 后为:\n{}".format(tt))

    # 查找一个存在的元素
    res = tt.search_string("print")
    print("查找存在的元素: print 结果为:\n{}".format(res))

    # 查找前缀元素
    res = tt.auto_complete("aa")
    print("查找前缀为 aa 的元素，结果为:\n{}".format(res))

    # 查找一个不存在的前缀元素
    res = tt.auto_complete("zzzzz")
    print("查找前缀不存在的 zzzzz 的元素，结果为:\n{}".format(res))

    # 删除单独串
    tt.delete_string("print")
    print("删除单独串: print 后为:\n{}".format(tt))

    # 删除前缀元素
    tt.delete_string("aaa")
    print("删除前缀串: aaa 后为:\n{}".format(tt))

    # 删除带有前缀的元素
    tt.delete_string("abcdef")
    print("删除带有前缀的串: abcdef 后为:\n{}".format(tt))

    # 删除最后一个元素时
    tt.clear()
    tt.add_string("abc")
    print("清空后加入一个串: abc 后为:\n{}".format(tt))

    tt.delete_string("abc")
    print("删除最后一个串的结果为:\n{}".format(tt))
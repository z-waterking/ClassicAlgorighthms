# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   AvlTree.py
@USER       :   ZZZZZ
@TIME       :   2021/4/25 10:32
'''

class Node(object):
    '''
    二叉树的结点
    '''
    def __init__(self, val = "", left = None, right = None):
        '''
        构造一个二叉树的结点
        :param val: 结点存储的值
        :param left: 结点的左子树
        :param right: 结点的右子树
        '''
        self.val = val
        self.left = left
        self.right = right


class AvlTree():
    '''
    平衡二叉查找树
    对于普通的二叉查找树来说，有一些较为特殊的情况，会使二叉查找树退化，查找操作变为线性查找
    例如，按顺序插入[1, 2, 3, 4, 5]，则可以想象，普通的二叉查找树会变成单侧树，每个结点都只有右子树。

    而平衡二叉树，所有的子结点均满足如下定义：
    1. 可以是空树。
    2. 假如不是空树，任何一个结点的左子树与右子树都是平衡二叉树，并且高度之差的绝对值不超过1。

    这样，就保证了在平衡二叉查找树中进行查找，时间复杂度为O(logN)

    二叉查找树最麻烦的地方在于：
    1. 插入结点时，如何保证相关结点平衡二叉树的性质。
    2. 删除结点时，如何保证相关结点平衡二叉树的性质。

    平衡二叉树的失衡调整主要是通过 ** 旋转最小失衡子树来实现的 **

    参考文献：
        https://www.cnblogs.com/suimeng/p/4560056.html

    '''
    def __init__(self):
        self.__root = None

# ---------------------------- 公有方法 ----------------------------

if __name__ == "__main__":
    tree = AvlTree()
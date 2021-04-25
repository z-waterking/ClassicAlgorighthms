# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   AVL_Tree.py
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


class AVL_Tree():
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
    def InitFromPreAndInOrder(self, preorder, inorder):
        '''
        从先序遍历和中序遍历列表构造二叉树,其中不要有重复的元素
        :param preorder: 先序遍历序列
        :param inorder: 中序遍历序列
        :return:
        '''
        if type(preorder) != list or type(inorder) != list:
            raise Exception("type must be list!")

        if len(preorder) != len(inorder):
            raise Exception("list must have same lenght!")

        def init_recursion(preorder, inorder):
            # base case, 当两个列表为空时，直接返回空
            if len(preorder) == 0 or len(inorder) == 0:
                return None

            # 新建当前的根结点
            root = Node(val = preorder[0])
            # 找到中序中相同元素的位置，以此位置将左右子树分开
            inorder_index = inorder.index(preorder[0])
            # -----------------------------------
            # 想象这样的情形：
            # 先序  1   2   3   4
            # 中序  3   2   1   4
            #             index
            # -----------------------------------
            root.left = init_recursion(preorder[1 : inorder_index + 1], inorder[ : inorder_index])
            root.right = init_recursion(preorder[inorder_index + 1 : ], inorder[inorder_index + 1 : ])
            return root

        self.__root = init_recursion(preorder, inorder)

    def InitFromInAndPostOrder(self, inorder, postorder):
        '''
            从中序遍历和后序遍历列表构造二叉树,其中不要有重复的元素
            :param preorder: 中序遍历序列
            :param postorder: 后序遍历序列
            :return:
        '''

        if type(inorder) != list or type(postorder) != list:
            raise Exception("type must be list!")

        if len(inorder) != len(postorder):
            raise Exception("list must have same lenght!")

        def init_recursion(inorder, postorder):
            # base case, 当两个列表为空时，直接返回空
            if len(inorder) == 0 or len(postorder) == 0:
                return None

            # 新建当前的根结点,为后序遍历的最后一个元素
            root = Node(val = postorder[-1])
            # 找到中序中相同元素的位置，以此位置将左右子树分开
            inorder_index = inorder.index(postorder[-1])
            # -----------------------------------
            # 想象这样的情形：
            # 后序  3   2   4   1
            # 中序  3   2   1   4
            #             index
            # -----------------------------------
            root.left = init_recursion(inorder[: inorder_index], postorder[: inorder_index])
            root.right = init_recursion(inorder[inorder_index + 1 : ], postorder[inorder_index: -1])
            return root

        self.__root = init_recursion(inorder, postorder)

    # --------------------- 递归遍历 -----------------------
    def pre_traverse_recursion(self):
        '''
        先序递归遍历
        :return: list，先序遍历结果
        '''
        res = []
        def pre_traverse(root):
            if root == None:
                return root
            nonlocal res
            # 访问结点
            res.append(root.val)
            # 遍历左子树
            pre_traverse(root.left)
            # 遍历右子树
            pre_traverse(root.right)

        pre_traverse(self.__root)

        return res

    def in_traverse_recursion(self):
        '''
        中序递归遍历
        :return: list，中序遍历结果
        '''
        res = []
        def in_traverse(root):
            if root == None:
                return root
            nonlocal res
            # 遍历左子树
            in_traverse(root.left)
            # 访问结点
            res.append(root.val)
            # 遍历右子树
            in_traverse(root.right)

        in_traverse(self.__root)

        return res

    def post_traverse_recursion(self):
        '''
        后序递归遍历
        :return: list, 后序遍历结果
        '''
        res = []
        def post_traverse(root):
            if root == None:
                return root
            nonlocal res
            # 遍历左子树
            post_traverse(root.left)
            # 遍历右子树
            post_traverse(root.right)
            # 访问结点
            res.append(root.val)

        post_traverse(self.__root)
        return res

    # --------------------- 非递归遍历 -----------------------
    def pre_traverse(self):
        '''
        利用栈进行先序非递归遍历
        :return: list, 先序遍历结果
        '''
        res = []
        # 构造一个栈
        stack = []
        root = self.__root

        while len(stack) != 0 or root != None:
            # 当root不空时，不断地去找左子树
            while root != None:
                # 入栈时访问
                res.append(root.val)
                stack.append(root)
                root = root.left

            #当root变为空时，需要出栈一个元素
            if len(stack) != 0:
                # 此时需要拿出栈中的最后一个元素
                # 往它的右子树走
                root = stack.pop()
                root = root.right
                # 之后它自己重新对右子树进行遍历

        return res

    def in_traverse(self):
        '''
        利用栈进行中序非递归遍历
        :return: list, 中序遍历结果
        '''
        res = []
        # 构造一个栈
        stack = []
        root = self.__root

        while len(stack) != 0 or root != None:
            # 当root不空时，不断地去找左子树
            while root != None:
                stack.append(root)
                root = root.left

            #当root变为空时，需要出栈一个元素
            if len(stack) != 0:
                # 此时需要拿出栈中的最后一个元素
                # 往它的右子树走
                root = stack.pop()
                # 出栈时访问
                res.append(root.val)
                root = root.right
                # 之后它自己重新对右子树进行遍历

        return res

    def post_traverse(self):
        '''
        利用栈进行非递归后序遍历
        :return: list, 后序遍历结果
        '''
        res = []
        stack = []
        root = self.__root
        # 前一个遍历的结点
        pre_node = None

        # 当root不为空时，不断向左走, 把左子结点全部入栈
        while root != None:
            stack.append(root)
            root = root.left

        while len(stack) != 0:
            # 这里把握住一个点：什么时候需要进行遍历？
            # 1. 没有右子树；2.右子树已遍历过
            root = stack[-1]
            if root.right == None or root.right == pre_node:
                # 遍历
                res.append(root.val)
                # pre_node更新
                pre_node = root
                # 从栈中删除
                stack.pop()
            else:
                root = root.right
                while root != None:
                    stack.append(root)
                    root = root.left

        return res

    def level_traverse(self):
        '''
        层序遍历
        :return: 层序遍历结果
        '''
        res = []
        # 借助队列实现
        root = self.__root
        queue = [root]

        while len(queue) != 0:
            # 这里嵌套一个循环，方便某些特定问题的解答
            # 例如要求每一层的和，则每次queue中的所有结点一定处于一层上
            # 要求树的最小高度，则每次可以保证访问一层的结点
            for i in range(len(queue)):
                root = queue.pop(0)
                # 层序遍历
                res.append(root.val)
                if root.left != None:
                    queue.append(root.left)
                if root.right != None:
                    queue.append(root.right)

        return res


# ---------------------------- 内部方法 ----------------------------
    def __str__(self):
        pre_res = self.pre_traverse_recursion()
        in_res = self.in_traverse_recursion()
        post_res = self.post_traverse_recursion()
        level_res = self.level_traverse()

        pre_res = ",".join([str(item) for item in pre_res])
        in_res = ",".join([str(item) for item in in_res])
        post_res = ",".join([str(item) for item in post_res])
        level_res = ",".join([str(item) for item in level_res])

        res = "先序: {}\n中序: {}\n后序: {}\n层序: {}".format(pre_res, in_res, post_res, level_res)

        return res

if __name__ == "__main__":
    tree = AVL_Tree()
    # 用前序遍历列表和中遍历列表进行初始化
    tree.InitFromPreAndInOrder([1, 2, 3, 4, 5, 6, 7], [3, 4, 2, 5, 1, 7, 6])
    print("前序+中序，初始化:\n{}".format(str(tree)))

    # 用中序遍历列表和后序遍历列表进行初始化
    tree.InitFromInAndPostOrder([3, 4, 2, 5, 1, 7, 6], [4, 3, 5, 2, 7, 6, 1])
    print("中序+后序，初始化:\n{}".format(str(tree)))

    # 检验非递归遍历的结果
    print("非递归先序遍历: {}".format(tree.pre_traverse()))
    print("非递归中序遍历: {}".format(tree.in_traverse()))
    print("非递归后序遍历: {}".format(tree.post_traverse()))
    print("层序遍历: {}".format(tree.level_traverse()))
# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   RedBlack_Tree.py
@USER       :   ZZZZZ
@TIME       :   2021/4/25 20:48
'''

class Node():
    def __init__(self, val = None, left = None, right = None, color = 'Black'):
        self.val = val
        self.left = left
        self.right = right

        # 包含自身的子树的 结点数量
        self.N = 1
        # 父结点指向它的链接颜色，默认是一条黑链
        self.color = color


class RedBlack_Tree():
    '''
    红黑树 与 2-3树可以 一一对应



    '''
    def __init__(self):
        self.__root = None

# ---------------------------- 公有方法 ----------------------------
    def init(self, values):
        '''
        从一个值列表构造一颗红黑树
        :param values: 值列表
        :return: None
        '''
        pass

    def insert(self, value):
        pass

    def delete(self, value):
        pass
    
    def _rotateLeft(self, node):
        '''
        将一个红色右链接的结点  旋转  成为一个红色左链接的结点
        node ->  E
               /   \\ <-> 红链
            el      S  <- new_node
                   /  \
                sl   sr

                 ⬇️

        new_node -> S
        红链 <-> //   \
                E     sr
              /  \
            el    sl

        :param node: 具有红色右链接的结点
        :return: 旋转后的根结点
        '''
        # 先把右结点取到
        new_node = node.right
        # 新结点的左结点 成为 原结点的右结点
        node.right = new_node.left
        # 转好新结点的左结点
        new_node.left = node

        # 变换新节点 旧结点 的颜色
        new_node.color = node.color
        node.color = 'Red'

        # 更新新旧结点所在子树的结点数量
        new_node.N = node.N
        node.N = 1 + node.left.N + node.right.N
        return new_node

    def _rotateRight(self, node):
        '''
        将一个红色左链接的结点  旋转  成为一个红色右链接的结点

                node -> S
            红链 <-> //   \
                    E     sr
                  /  \
                el    er

                    ⬇️

        new_node ->  E
                   /   \\ <-> 红链
                el      S  <- node
                       /  \
                    er     sr

        :param node: 具有红色左链接的结点
        :return: 旋转后的根结点
        '''
        # 先把左结点取到
        new_node = node.left
        # 新结点的左结点 成为 原结点的右结点
        node.left = new_node.right
        # 转好新结点的右结点
        new_node.right = node

        # 变换新节点 旧结点 的颜色
        new_node.color = node.color
        node.color = 'Red'

        # 更新新旧结点所在子树的结点数量
        new_node.N = node.N
        node.N = 1 + node.left.N + node.right.N
        return new_node

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
    pass

# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   RedBlackTree.py
@USER       :   ZZZZZ
@TIME       :   2021/4/25 20:48
'''

class Node():
    def __init__(self, key = None, val = None, left = None, right = None, N = 1, color = 'Black'):
        '''
        初始化一个红黑树的结点
        :param key: 结点的索引，用以比较结点
        :param val: 结点中存储的值
        :param left: 结点的左子树
        :param right: 结点的右子树
        :param N: 当前结点所在的子树的结点数量
        :param color: 当前结点的颜色：红/黑
        '''
        self.key = key
        self.val = val
        self.left = left
        self.right = right

        # 包含自身的子树的 结点数量
        self.N = N
        # 父结点指向它的链接颜色，默认是一条黑链
        self.color = color

    def flipColors(self):
        '''
        将左右结点由红转黑，将自己由黑转红
        :return: None
        '''
        if self.left != None:
            self.left.color = 'Black'

        if self.right != None:
            self.right.color = 'Black'

        self.color = 'Red'

# ---------------------------- 辅助函数 ----------------------------
def isRed(node):
    '''
    判断结点的颜色
    :return: 如果是红节点，返回True；否则，返回Fasle
    '''
    # 如果是个空结点，则为黑色
    if node == None:
        return False

    if node.color == 'Red':
        return True
    else:
        return False

# ---------------------------- 红黑树 ----------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------
class RedBlackTree():
    '''
    红黑树 与 2-3树可以 一一对应


    参考文献:
        1. 史上最清晰的红黑树讲解（上):  http://mt.sohu.com/20161014/n470317653.shtml
        2. 史上最清晰的红黑树讲解（下)：  https://www.sohu.com/a/116478983_355142
        3. 《算法4》代码：https://algs4.cs.princeton.edu/code/
    '''
    def __init__(self):
        self.__root = None

# ---------------------------- 公有方法 ----------------------------
    def init(self, keys, values):
        '''
        从一个值列表构造一颗红黑树
        :param values: 值列表
        :return: None
        '''
        # 将数据逐个插入
        # 暂时以value作为它本身的key
        for key, value in zip(keys, values):
            self.insert(key, value)

    def insert(self, key, value):
        '''
        递归向红黑树中插入一个结点
        :param key: 待插入的key值
        :param value: 待插入的value值
        :return: None
        '''
        def put(node, key, value):
            '''
            将value插入以node为根的红黑树中
            :param node: 子树的根
            :param value: 待插入的值
            :return:
            '''
            # 如果找到了空节点，向其中插入红色结点
            if node == None:
                return Node(key = key, val = value, N = 1, color = 'Red')

            if key < node.key:
                # 向左子树中插入
                node.left = put(node.left, key, value)
            elif key > node.key:
                # 向右子树中插入
                node.right = put(node.right, key, value)
            else:
                # 更新结点的值
                node.val = value

            # 假装现在左、右子树已经全部插入好了
            # 插入的结点一定是一个 红链接
            # 则插入后可能情况如下：
            # 1. 红链接插在了2（黑）结点的左边，则符合条件，不用操作

            # 2. (1) 红链接插在了3（红）结点的中间    <->    State3: 如果左黑，右红，则左旋，这样转换为 State2
            #
            #    (2) 红链接插在了2（黑）结点的右边, 一次左旋即可修复
            if isRed(node.left) == False and isRed(node.right) == True:
                node = self._rotateLeft(node)

            # 3. 红链接插在了3（红）结点的左边   <->   State2: 如果左红，且左边的左子结点也是红的，则右旋，旋转后转换为 State1
            if isRed(node.left) == True and isRed(node.left.left) == True:
                node = self._rotateRight(node)

            # 4. 红链接插在了3（红）结点的右边   <->   State1: 如果左红 且 右红，则改变node，node.left, node.right的颜色, 根节点变为红，将红色向上传递
            if isRed(node.left) == True and isRed(node.right) == True:
                node.flipColors()

            # 更新node的N值,左右孩子可能为空，因此要判断
            node.N = 1
            if node.left != None:
                node.N += node.left.N
            if node.right != None:
                node.N += node.right.N

            return node

        # 将value放入根结点
        self.__root = put(self.__root, key, value)
        # 每次插入完成后，将根节点设为黑色
        self.__root.color = 'Black'

    def deleteMin(self):
        '''
        删除红黑树中的最小值
        :return:
        '''

        # 如果root的左右子结点颜色为黑，将其变红
        if isRed(self.__root.left) == False and isRed(self.__root.right) == False:
            self.__root.color = 'Red'

        self.__root = self._delMin(self.__root)

        if(self.__root != None):
            self.__root.color = 'Black'

    def deleteMax(self):
        '''
        删除红黑树中的最大值
        :return:
        '''
        if isRed(self.__root.left) == False and isRed(self.__root.right) == False:
            self.__root.color = 'Red'

        self.__root = self._delMax(self.__root)

        if self.__root != None:
            self.__root.color = 'Black'

    def delete(self, key, value):
        '''
        删除红黑树中具体的key
        :param key:
        :param value:
        :return:
        '''
        # 没查到，直接返回
        if self.search(key) == False:
            return

        if isRed(self.__root.left) == False and isRed(self.__root.right) == False:
            self.__root.color = 'Red'

        self.__root = self._del(self.__root, key)

        if self.__root != None:
            self.__root.color = 'Black'

    def getMin(self):
        '''
        取得树中的最小结点
        :return:
        '''
        return self._MinNode(self.__root)

    def getMax(self):
        '''
        取得树中的最大结点
        :return:
        '''

        return self._MaxNode(self.__root)

    def search(self, key):
        '''
        在红黑树中查询子节点
        :param key: 要查找的key值
        :return: 查找到的value值
        '''
        node = self.__root
        while node != None:
            if node.key == key:
                return node.val
            elif key < node.key:
                node = node.left
            else:
                node = node.right

        # 没查到，返回None
        return None

# --------------------- 私有方法 -----------------------
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

        # 更新node的N值,左右孩子可能为空，因此要判断
        node.N = 1
        if node.left != None:
            node.N += node.left.N
        if node.right != None:
            node.N += node.right.N

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

        # 更新node的N值
        node.N = 1
        if node.left != None:
            node.N += node.left.N
        if node.right != None:
            node.N += node.right.N

        return new_node

    def _moveRedLeft(self, node):
        '''
        将右、左子树的红色链接转上来
            // or \\  <-> 红链接

           node -> S
                 /   \
                sl     sr
                     //  \
                  srl    srr
                /   \
              srll  srlr

                    ⬇️

                第一次旋转
            node -> S
                  /   \
                sl    srl
                     /   \\
                  srll    sr
                        /   \
                     srlr   srr

                     ⬇️

                第二次旋转
                   srl
                /       \\
               S          sr
             /  \         /  \
            sl   srll   srlr   srr

        :param node:
        :return:
        '''
        node.flipColors()

        if node.right != None and isRed(node.right.left) == True:
            node.right = self._rotateRight(node.right)
            node = self._rotateLeft(node)
            node.flipColors()

        return node

    def _moveRedRight(self, node):
        '''
        将左、左子树的红色链接转上来
        // or \\  <-> 红链接

               node ->  S
                     /    \
                   sl       sr
                 //   \    /  \
               sll   slr  srl  srr

                        ⬇️

                        sl
                     //     \
                   sll       S
                            /  \
                           slr  sr
                              /  \
                             srl  srr

        :param node:
        :return:
        '''
        node.flipColors()

        if node.left != None and isRed(node.left.left):
            node = self._rotateRight(node)
            node.flipColors()

        return node

    def _delMin(self, node):
        '''
        删除以node为根的红黑树的最小结点
        :param node:
        :return:
        '''
        if node.left == None:
            return None

        # 把右、左子树的红链接转上来
        if isRed(node.left) == False and isRed(node.left.left) == False:
            node = self._moveRedLeft(node)

        node.left = self._delMin(node.left)

        return self._balance(node)

    def _delMax(self, node):
        '''
        删除以node为根的树下键值最大结点
        :param node:
        :return:
        '''
        if isRed(node.left):
            node = self._rotateRight(node)

        if node.right == None:
            return None

        if isRed(node.right) == False and isRed(node.right.left) == False:
            node = self._moveRedRight(node)

        node.right = self._delMax(node.right)

        return self._balance(node)

    def _del(self, node, key):
        '''
        删除以node为根的树下键为key的结点
        :param node:
        :param key:
        :return:
        '''
        if key < node.key:
            # 向左删除
            if isRed(node.left) == False and isRed(node.left.left) == False:
                node = self._moveRedLeft(node)

            node.left = self._del(node.left, key)
        else:
            if isRed(node.left) == True:
                node = self._rotateRight(node)

            if key == node.key and node.right == None:
                return None

            if isRed(node.right) == False and isRed(node.right.left):
                node = self._moveRedRight(node)

            if key == node.key:
                x = self._MinNode(node.right)
                node.key = x.key
                node.val = x.val
                node.right = self._delMin(node.right)
            else:
                node.right = self._del(node.right, key)

        return self._balance(node)

    def _MinNode(self, node):
        '''
        获取以node为根的树下最小结点
        :param node:
        :return:
        '''
        if node.left == None:
            return node
        else:
            return self._MinNode(node.left)

    def _MaxNode(self, node):
        '''
        获取以node为根的树下最大结点
        :param node:
        :return:
        '''
        if node.left == None:
            return node
        else:
            return self._MaxNode(node.right)

    def _balance(self, node):
        '''
        对node结点进行平衡操作
        :param node:
        :return:
        '''
        if isRed(node.right) == True and isRed(node.left) == False:
            node = self._rotateLeft(node)

        if isRed(node.left) == True and isRed(node.left.left) == True:
            node = self._rotateRight(node)

        if isRed(node.left) == True and isRed(node.right) == True:
            node.flipColors()

        # 更新node的N值,左右孩子可能为空，因此要判断
        node.N = 1
        if node.left != None:
            node.N += node.left.N
        if node.right != None:
            node.N += node.right.N

        return node

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
            res.append((root.val))
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
    rbt = RedBlackTree()
    # 从列表初始化红黑树
    rbt.init([5, 7, 8, 9, 0, 1, 2], [5, 7, 8, 9, 0, 1, 2])
    print("初始化后的红黑树为:\n{}".format(rbt))

    # 向红黑树中插入一个结点
    rbt.insert(10, 10)
    print("插入结点后的红黑树为:\n{}".format(rbt))

    # 查找红黑树中的结点
    res = rbt.search(10)
    print("查得的结点值为: {}".format(res))

    # 删除红黑树中的最小结点
    rbt.deleteMin()
    print("删除最小结点后为: \n{}".format(rbt))

    # 删除红黑树中的最小结点
    rbt.deleteMin()
    print("删除最小结点后为: \n{}".format(rbt))

    # 删除红黑树中的特定结点
    rbt.delete(9, 9)
    print("删除最小结点后为: \n{}".format(rbt))


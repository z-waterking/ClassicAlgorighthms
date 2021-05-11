# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   UnionFind.py
@USER       :   ZZZZZ
@TIME       :   2021/5/11 16:04
'''
class UnionFind():
    '''
    并查集:
    主要用来解决 "动态连通性" 问题
    可以想象一张地图上有很多点，有些点之间是有道路相互联通的，而有些点则没有。
    如果我们现在要从点A走向点B，那么一个关键的问题就是判断我们能否从A走到B呢？
    换句话说，A和B是否是连通的。
    这是动态连通性最基本的诉求。
    现在给出一组数据，其中每个元素都是一对“点”，表示形式为:(p, q)，代表这对点之间是联通的，
    且具有三个性质：
        自反性：p和p是相连的
        对称性：如果p和q相连，则q和p相连
        传递性：如果p和q相连，q和r相连，那么p和r相连

    我们需要设计一个算法，让计算机依次读取这些数据，最后判断出其中任意两点是否连通。
    '''
    def __init__(self):
        # 每个结点所在的连通分量标记
        # self.ids[2] = 2 代表2号结点所在的连通分量标记为 2
        self.ids = []
        self.size = []

        # 不同连通分量的数量
        self.count = 0

# ---------------------------- 公有方法 ----------------------------
    def init(self, N):
        '''
        初始化结点
        :param N: 并查集中的结点个数
        :return: None
        '''
        # 初始化每个结点所在的连通分量标识
        self.ids = list(range(N))

        self.size = [1] * N
        self.count = N

# ---------------------------- quick-find 实现 ----------------------------
    '''
        ids的含义是: 其中的每个值都是这个结点所在的连通连通分量的标识
        例：
        id      0   1   2   3   4
        value   1   1   1   3   3
        表明：0，1，2结点为同一个连通分量， 3，4为同一个连通分量
        
        find操作速度很快
        但是union需要扫描整个ids数组
        如果最终得到的连通集很少，那么quick-find的运行时间是平方级的
    '''
    def union_v1(self, p, q):
        '''
        将p和q所在的连通分量进行连通
        :param p: 待连通的第一个结点
        :param q: 待连通的第二个结点
        :return:
        '''

        pID = self.find_v1(p)
        qID = self.find_v1(q)

        # 如果p和q本身就属于同一个连通分量，则跳过
        if pID == qID:
            return

        # 将p的连通分量重命名为q的标识
        for i in range(len(self.ids)):
            if self.ids[i] == pID:
                self.ids[i] = qID

        # 减少一个连通分量
        self.count -= 1

    def find_v1(self, p):
        '''
        查找p所在的连通分量标识
        :param p: 结点
        :return: 结点所在的连通分量
        '''
        return self.ids[p]

# ---------------------------- quick-union 实现 ----------------------------
    '''
        ids的含义是: 其中的每个值都是与当前结点在同一个连通分量中的另一个结点的id
        例：
        id      0   1   2   3   4
        value   1   2   2   4   4
        表明：0，1，2结点为同一个连通分量， 3，4为同一个连通分量
        
        这种方法希望提高union的速度,进行union操作仅需要修改指向的结点
        它实质上是构造了一个森林，每个结点都指向了自己的父节点，根结点是这个连通集合的标识
        
        但是进行find操作的最坏情况需要遍历整个数组
        如果最终得到的连通集很少，那么quick-find的运行时间是平方级的
        
    '''
    def union_v2(self, p, q):
        '''
        将p和q所在的连通分量进行连通
        :param p: 待连通的第一个结点
        :param q: 待连通的第二个结点
        :return:
        '''
        # 找到p与q的连通分量id
        pRoot = self.find_v2(p)
        qRoot = self.find_v2(q)

        if pRoot == qRoot:
            return
        # 将所在的连通分量链接到q的连通分量上
        self.ids[pRoot] = qRoot

        self.count -= 1

    def find_v2(self, p):
        '''
        找出p对应的连通分量
        :param p: 
        :return: 
        '''
        # 一直向后找，直到找到结点id与分量id相同的那个结点
        while p != self.ids[p]:
            p = self.ids[p]

        return p

# ---------------------------- 加权 quick-union 实现 ----------------------------
    '''
        ids的含义是: 其中的每个值都是与当前结点在同一个连通分量中的另一个结点的id
        size的含义是：每个以此结点为根的连通分量的大小
        例：
        id      0   1   2   3   4
        value   1   2   2   4   4
        size    1   1   3   1   2
        表明：0，1，2结点为同一个连通分量， 3，4为同一个连通分量

        这种方法在quick-union的基础上，进行链接操作时，将较小的树作为较大的树的根节点
        
        它可以使得树的高度增长不会太快，保证了 ** 对数级别 ** 的性能

    '''

    def union_v3(self, p, q):
        '''
        将p和q所在的连通分量进行连通
        :param p: 待连通的第一个结点
        :param q: 待连通的第二个结点
        :return:
        '''
        # 找到p与q的连通分量id
        pRoot = self.find_v3(p)
        qRoot = self.find_v3(q)

        if pRoot == qRoot:
            return
        # 与quick-union不同的是，需要判断哪个树比较大
        # 我们将小树的根节点链接到大树的根节点
        if self.size[pRoot] < self.size[qRoot]:
            # 链接根结点
            self.ids[pRoot] = qRoot
            self.size[qRoot] += self.size[pRoot]
        else:
            # 链接根节点
            self.ids[qRoot] = pRoot
            self.size[pRoot] += self.size[qRoot]

        self.count -= 1

    def find_v3(self, p):
        '''
        找出p对应的连通分量
        :param p:
        :return:
        '''
        # 一直向后找，直到找到结点id与分量id相同的那个结点
        while p != self.ids[p]:
            p = self.ids[p]

        return p

    def is_connected(self, p, q):
        '''
        判断结点是否连通
        :param p: 第一个结点
        :param q: 第二个结点
        :return: 如果存在于同一个连通分量中，返回True；否则，False
        '''
        if self.find_v1(p) == self.find_v1(q):
            return True
        else:
            return False

    def count(self):
        '''
        连通结点组成的不同的连通分量数量
        :return: 连通结点组成的不同的连通分量数量
        '''
        return self.count

# ---------------------------- 内部方法 ----------------------------
    def __str__(self):
        '''
        直接将并查集进行打印
        :return:
        '''
        res = ''
        for i in range(len(self.ids)):
            res += '{}:{}\t'.format(i, self.ids[i])
        res += '\n'

        res += '不同集合的数量为{}'.format(self.count)
        return res

if __name__ == "__main__":
    uf = UnionFind()
    # 结点参数
    N = 10
    points = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9), (5, 0), (7, 2), (6, 1), (1, 0), (6, 7)]

    # quick-find 测试
    print("quick-find 测试")
    uf.init(N)
    for p, q in points:
        uf.union_v1(p, q)
    print("并差集的结果为:\n{}".format(uf))
    print("判断两个结点是否连通的结果为:{}".format(uf.is_connected(0, 1)))

    # quick-union测试
    print("quick-union 测试")
    uf.init(N)
    for p, q in points:
        uf.union_v2(p, q)
    print("并差集的结果为:\n{}".format(uf))
    print("判断两个结点是否连通的结果为:{}".format(uf.is_connected(0, 1)))

    # 加权quick-union测试
    print("加权quick-union 测试")
    uf.init(N)
    for p, q in points:
        uf.union_v3(p, q)
    print("并差集的结果为:\n{}".format(uf))
    print("判断两个结点是否连通的结果为:{}".format(uf.is_connected(0, 1)))
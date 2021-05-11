# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   UndirectedGraph.py
@USER       :   ZZZZZ
@TIME       :   2021/5/6 10:55
'''

class UndirectedGraph:
    '''
    带权无向图

    用邻接矩阵进行存储的图。

    用prim算法实现寻找连通图的最小生成树。
    '''
    def __init__(self, num_nodes):
        '''
        构造空图
        :param num_nodes: 图中的结点数量
        '''
        self.num_nodes = num_nodes
        self.num_edges = 0

        # 存储每个结点的度
        self.degress = [0] * self.num_nodes

        # 构造初始化为0的图
        self.matrix = []
        for i in range(self.num_nodes):
            self.matrix.append([0] * self.num_nodes)

# ---------------------------- 公有方法 ----------------------------
    def init(self, edges):
        '''
        通过传入边的列表来构造图
        :param edges: 一系列边，以元组形式给入，（u, v, weight)
        :return:
        '''
        for u, v, weight in edges:
            self.insert(u, v, weight)

    def insert(self, u, v, weight):
        '''
        向图中插入一条边
        :param u: 起始结点
        :param v: 终止结点
        :param weight: 权重
        :return: None
        '''
        # 判断是否超出边界
        if self._check_edge_valid(u, v) \
        and self._check_weight_valid(weight) == True:
            # 插入结点
            self.matrix[u][v] = weight

            # 更新边及各结点的度
            self.num_edges += 1
            self.degress[u] += 1
            self.degress[v] += 1

    def delete(self, u, v):
        '''
        从图中删除一条边
        :param u: 起始结点
        :param v: 终止结点
        :return: None
        '''
        # 判断是否超出边界
        if self._check_edge_valid(u, v):
            self.matrix[u][v] = 0

            # 更新边及各结点的度
            self.num_edges -= 1
            self.degress[u] -= 1
            self.degress[v] -= 1

    def get_degree(self, u):
        '''
        取得结点的度
        :param u: 结点编号
        :return: 对应的度
        '''
        if self._check_node_valid(u) == True:
            return self.degress[u]

    def get_weight(self, u, v):
        '''
        取得对应边的权重
        :param u: 起始结点
        :param v: 终止结点
        :return: weight
        '''
        if self._check_edge_valid(u, v) == True:
            return self.matrix[u][v]

    def get_edge_count(self):
        '''
        取得边的数量
        :return: 图中边的数量
        '''
        return self.num_edges

    def is_connected(self):
        '''
        判断是否是连通图
        :return: 如果是连通图，返回True；否则，返回False
        '''
        # 基础判断，如果没有边，或者边的数量少于结点数-1，必然不可能连通
        if self.num_edges == 0 or self.num_edges < self.num_nodes - 1:
            return False

        visited = [False] * self.num_nodes
        def dfs(node):
            '''
            从node结点开始进行深度优先访问，将访问过的所有结点进行标记
            :param node: 起始结点
            :return: None
            '''
            nonlocal visited
            visited[node] = True

            for target in range(self.num_nodes):
                if self.matrix[node][target] != 0 and visited[target] == False:
                    dfs(target)

        # 从0开始进行深度优先遍历
        dfs(0)

        # 遍历结束后检查visited数组
        if visited.count(False) == 0:
            return True
        else:
            return False

    def prim(self, node):
        '''
        用prim算法寻找最小生成树

        加点法，挨个去查找与当前最小生成树相连的权重最小的点，找到则将其加入

        :param node: 起始结点
        :return: 最小生成树的权重
        '''
        # 用来判断是否存在于最小生成树中
        flag = [False] * self.num_nodes
        res = 0

        # 待选集合，保存接下来要搜寻的结点以及对应的连接权重
        # *** 注：这里待选集合的目的是希望找到与整个树相连的所有边中最小的那个权重
        # *** 因此如果能使用优先队列，保证可以快速地查找到最小权重，
        # *** 则可以大幅度降低时间复杂度 ***
        node_weight = []

        # 将当前结点加入
        flag[node] = True
        key = node

        for i in range(self.num_nodes - 1):
            # 将所有与key相连的边都加入待选集合中
            for to in range(self.num_nodes):
                # 将结点加入队列
                if flag[to] == False and self.matrix[key][to] != 0:
                    node_weight.append((to, self.matrix[key][to]))

            # *** 对nodes进行排序，找到其中最小的那个权重 ***
            node_weight.sort(key = lambda x:x[1])

            # 将其中已经存在于最小生成树中的边去掉
            while len(node_weight) != 0 and flag[node_weight[0][0]] == True:
                node_weight.pop(0)

            # 如果已经空了，表示没有需要加入的边了
            if len(node_weight) == 0:
                break

            # 将权重最小的那个取出，权重加到结果上，更新key
            node = node_weight.pop(0)
            key = node[0]
            res += node[1]

        return res

    def clear(self):
        '''
        清空图
        :return: None
        '''
        # 重新初始化一下
        num_nodes = self.num_nodes
        self.__init__(num_nodes)

# ---------------------------- 私有方法 ----------------------------
    def _check_edge_valid(self, u, v):
        '''
        检查一对边是否合法
        :param u: 起点
        :param v: 终点
        :return: 如果合法，返回True；否则，返回False
        '''
        if self._check_node_valid(u) == True \
        and self._check_node_valid(v) == True \
        and u != v:
            return True

    def _check_node_valid(self, node):
        '''
        检查结点是否合法
        :param node: 输入的结点
        :return: 如果合法，返回True；否则，返回False
        '''
        if node < 0 or node >= self.num_nodes:
            raise Exception("invalid edges")

        return True

    def _check_weight_valid(self, weight):
        '''
        检查权重是否合法
        :param weight: 权重
        :return: 如果合法，返回True；否则，返回False
        '''
        if weight <= 0:
            raise Exception("invalid weight")

        return True

# ---------------------------- 内部方法 ----------------------------
    def __str__(self):
        res = ''
        for i in range(self.num_nodes):
            for j in range(self.num_nodes):
                res += "{:4}\t".format(self.matrix[i][j])
            res += "\n"

        return res

if __name__ == "__main__":
    # 图有12个结点
    ug = UndirectedGraph(12)

    # 初始化结点
    edges = [(2,3,68.84),(10,1,11.37),(11,0,65.73),(2,8,48.48),(6,5,47.40),(8,4,85.81),(6,9,57.11),(6,1,75.85),(3,9,81.33),(8,7,3.78),(1,1,68.25),(4,10,55.64),(5,6,25.59), (1,4,89.77),(6,4,78.54),(6,7,49.28),(7,3,4.92),(9,5,15.76),(8,8,75.56),(6,11,18.28),(6,9,18.07),(7,9,30.65),(7,10,32.08),(9,6,84.24),(1,2,81.11),(8,6,36.75),(3,5,10.80),(5,5,85.90),(7,6,54.21),(6,7,22.69),(8,3,49.54),(7,2,3.18),(11,11,10.93),(2,10,67.42),(6,8,90.65),(2,10,17.63),(4,5,51.63),(0,11,6.10),(0,3,12.92),(8,10,96.68),(7,6,81.01),(0,9,66.71),(6,3,26.18),(2,4,47.30),(10,7,9.07),(2,3,54.87),(6,10,57.60),(11,8,19.06),(2,5,57.96)]
    ug.init(edges)
    print("初始化后的图为:\n{}".format(ug))

    # 插入一条边
    ug.insert(0, 1, 20)
    print("插入边后的图为:\n{}".format(ug))

    # 删除一条边
    ug.delete(0, 3)
    print("删除边后的图为:\n{}".format(ug))

    # 获取各项指标
    degree = ug.get_degree(0)
    weight = ug.get_weight(1, 2)
    num_edges = ug.get_edge_count()
    print("结点 0 的度为: {}".format(degree))
    print("边 1，2 的权重为: {}".format(weight))
    print("图中边的数量为: {}".format(num_edges))

    # 判断图是否连通
    cn = ug.is_connected()
    print("图的连通性为: {}".format(cn))

    # 获取最小生成树
    mst = ug.prim(0)
    print("图的最小生成树的权重为: {}".format(mst))



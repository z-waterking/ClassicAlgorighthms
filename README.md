# 目录

<table border=0.1 cellspacing=0 width="90%">
<tr><td width="200">算法</td><td width="200">内容</td><td width="300">实现</td></tr>
<tr><td rowspan=11><a href="#数据结构">数据结构</a></td><td rowspan=4><a href="#表">表</a></td><td>单链表</td></tr>
<tr><td>双向链表</td></tr>
<tr><td>哈希表</td></tr>
<tr><td>最小栈</td></tr>
<tr><td rowspan=5><a href="#树">树</a></td><td>二叉树</td></tr>
<tr><td>字典树</td></tr>
<tr><td>红黑树</td></tr>
<tr><td>二叉平衡树</td></tr>
<tr><td>堆</td></tr>
<tr><td rowspan=2><a href="#图">图</a></td><td>并查集</td></tr>
<tr><td>无向图</td></tr>
<tr><td rowspan=14><a href="#经典算法">经典算法</a></td><td rowspan=9><a href="#排序算法">排序算法</a></td><td>冒泡排序</td></tr>
<tr><td>选择排序</td></tr>
<tr><td>插入排序</td></tr>
<tr><td>普通&nbsp;/&nbsp;3向切分&nbsp;快速排序</td></tr>
<tr><td>递归&nbsp;/&nbsp;非递归&nbsp;归并排序</td></tr>
<tr><td>计数）/&nbsp;桶排序</td></tr>
<tr><td>堆排序</td></tr>
<tr><td>希尔排序</td></tr>
<tr><td>基数排序</td></tr>
<tr><td rowspan=2><a href="#搜索算法">搜索算法</a></td><td>二分查找</td></tr>
<tr><td>二分查找左右边界</td></tr>
<tr><td rowspan=3><a href="#回溯算法">回溯算法</a></td><td>子集</td></tr>
<tr><td>组合</td></tr>
<tr><td>全排列</td></tr>
<tr><td></td><td><a href="#其他算法">其他算法</a></td><td></td></tr>
<tr><td><a href="#LeetCode">LeetCode</a></td><td></td><td></td></tr>
</table>
<hr/>

<h1 id="数据结构">数据结构</h1>

## 写在前面：

数据结构是计算机的基础课。其底层存储只有2种类型，顺序存储和链式存储。

因此，我这里实现的数据结构，没有用到第三方包的实现，完全利用最原始的方法来实现常用的数据结构，以及基于其上的一些算法。

虽然整个项目是用python实现的，但中间未使用”奇技淫巧“，只要方法正确，可以很快速地扩展到其他语言。

## 缺失之处：

参数校验：这是一个非常麻烦的工作，用户可能输入的情况千奇百怪，因此参数校验只做了最基础的部分。

可扩展性：每个文件内都有各自类的测试。并没有去实现一个模板支持各种情况。例如：堆中实现的是大根堆。若构造时传入比较函数，则可扩展为小根堆。

## 目录

### 表

* [单链表](/DataStructure/Table/SingleLinkedList.py)

  * 从传入的列表中构造单链表
  * 头插一个元素
  * 尾插一个元素
  * 向中间指定位置插入元素
  * 删除头部元素
  * 删除尾部元素
  * 删除指定中间位置的元素
  * 查找某个元素是否存在
  * 递归反转整个链表

* [双向链表](/DataStructure/Table/DeLinkedList.py)

  * 从传入的列表中构造双向链表
  * 头插一个元素
  * 尾插一个元素
  * 向中间指定位置插入元素
  * 删除头部元素
  * 删除尾部元素
  * 删除指定中间位置的元素
  * 查找某个元素是否存在

* [哈希表](/DataStructure/Table/HashTable.py)

  * 通过一个列表构造哈希表
  * 向哈希表中插入一个值
  * 从哈希表中删除一个值
  * 哈希表中查找一个值
  * 哈希函数，通过给定的值，计算出一个位置

* [最小栈](/DataStructure/Table/MinStack.py)

  * 从传入的列表中构造最小栈
  * 插入一个元素
  * 弹出一个元素
  * 取得最小元素
  * 清空所有元素

### 树

* [二叉树](/DataStructure/Tree/BinaryTree.py)

  * 从先序列表和中序列表构造二叉树
  * 二叉树的先序递归遍历
  * 二叉树的中序递归遍历
  * 二叉树的后序递归遍历
  * 二叉树的先序非递归遍历
  * 二叉树的中序非递归遍历
  * 二叉树的后序非递归遍历
  * 二叉树的层序遍历

* [字典树](/DataStructure/Tree/TrieTree.py)

  * 通过strings_list构造一颗字典树
  * 增加一个串
  * 查找字典树中是否存在对应串
  * 查找与prefix具有相同前缀的串
  * 删除字典树中的串
  * 获取字典树中的串的数量
  * 清空所有元素
  * 遍历以node为结点的整个字典树

* [红黑树](/DataStructure/Tree/RedBlackTree.py)

  * 从一个值列表构造一颗红黑树
  * 递归向红黑树中插入一个结点
  * 在红黑树中查询子节点
  * 将一个红色右链接的结点  旋转  成为一个红色左链接的结点
  * 将一个红色左链接的结点  旋转  成为一个红色右链接的结点
  * 红黑树的先序递归遍历
  * 红黑树的中序递归遍历
  * 红黑树的后序递归遍历
  * 红黑树的先序非递归遍历
  * 红黑树的中序非递归遍历
  * 红黑树的后序非递归遍历
  * 红黑树的层序遍历
  
* [二叉平衡树](/DataStructure/Tree/AvlTree.py)

  * TODO

* [堆](/DataStructure/Tree/Heap.py)

  * 通过数组构造一个堆
  * 向堆中插入一个元素
  * 取出堆顶元素
  * 判断堆是否是空的
  * 清空所有元素
  * 将数组变成一个堆
  * 堆中index结点上浮
  * 堆中index结点下沉

### 图

* [并查集](/DataStructure/Graph/UnionFind.py)

  * 初始化结点
  * 采用quick-find方式实现union find
  * 采用quick-union方式实现union find
  * 采用加权quick-union方式实现union find
  * 判断两个结点是否连通
  * 连通结点组成的不同的连通分量数量

* [无向图](/DataStructure/Graph/UndirectedGraph.py)

  * 通过传入边的列表来构造图
  * 向图中插入一条边
  * 从图中删除一条边
  * 取得结点的度
  * 取得对应边的权重
  * 取得边的数量
  * 判断是否是连通图
  * 用prim算法寻找最小生成树
  * 清空图

## 数据结构思维导图
![Image text](images/DataStructure.jpeg)

# 经典算法

## 目录

### 排序算法

* [冒泡排序](/Algorighms/Sort/BubbleSort.py)
* [选择排序](/Algorighms/Sort/SelectionSort.py)
* [插入排序](/Algorighms/Sort/InsertSort.py)
* [快速排序](/Algorighms/Sort/QuickSort.py)
* [归并排序](/Algorighms/Sort/MergeSort.py)
* [（计数）/ 桶排序](/Algorighms/Sort/BucketSort.py)
* [堆排序](/Algorighms/Sort/HeapSort.py)
* [希尔排序](/Algorighms/Sort/ShellSort.py)
* [基数排序](/Algorighms/Sort/RadixSort.py)

#### 各排序算法时间复杂度

![Image text](images/SortAlgorithms.png)

### 搜索算法

* [二分查找](/Algorighms/Search/BinarySearch.py)
* [二分查找左右边界](/Algorighms/Search/BinarySearch.py)

### 回溯算法

* [子集](/Algorighms/BackTrack/SubSet.py)
* [组合](/Algorighms/BackTrack/Combination.py)
* [全排列](/Algorighms/BackTrack/Permutations.py)

### 其他算法

* [伪随机数构造]

# leetcode

包括了leetcode刷题结果。

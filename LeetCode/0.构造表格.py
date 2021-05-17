# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   0.构造表格.py
@USER       :   ZZZZZ
@TIME       :   2021/5/17 17:57
'''

import os
# 把所有文件名排序
files = os.listdir()
files.sort(key = lambda x:int(x.split('.')[0]))

# 构造表格
res = "|题目|链接| \n |:--|:--| \n"
for filename in files:
    res += "|{}|[{}](/LeetCode/{})|\n".format(filename, filename, filename)

print(res)
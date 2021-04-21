#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        li = [0]
        le = 20
        columns = {}
        def add_norm2_summary(columns):
            for column in sorted(set(columns), key=lambda x: x.key):
                try:
                    dim = column.dimension
                except:
                    dim = column.embedding_dimension

        def add_embed_layer_norm_batch(layer_tensor, columns, model_name=""):
            monitor_dict = {}
            if layer_tensor is None:
                return
            i = 0
            for column in sorted(set(columns), key=lambda x: x.key):
                try:
                    dim = column.dimension
                except:
                    dim = column.embedding_dimension
                monitor_dict[model_name + "." + column.name] = tf.norm(layer_tensor[:, i:i + dim], axis=-1)
                i += dim
            return monitor_dict

        for i, t in enumerate(li):
            '''
                switch the indexs larger than le
            '''
            if i > le:
                try:
                    dim = column.dimension
                except:
                    try:
                        dim = column.embedding_dimension
                    except:
                        dim = len(column.boundaries) + 1
            else:
                continue
        res = []
        dic = {}
        for i, num in enumerate(nums):
            d = target - num
            if d in dic:
                res = [i, dic[d]]
            dic[num] = i
        return res
# @lc code=end


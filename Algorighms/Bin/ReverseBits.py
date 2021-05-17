# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   ReverseBits.py
@USER       :   ZZZZZ
@TIME       :   2021/5/17 21:23
'''

class ReverseBits():
    def __init__(self):
        pass

    def Solution(self, num):
        '''
        将十进制数的二进制表示翻转
        :param num: 待翻转数字
        :return: 二进制翻转后的数字
        '''
        res = 0
        while True:
            if num == 0:
                break
            # res左移，腾出一个位置
            res = res << 1
            # num & 1 取出num的最后一位
            res = res + (num & 1)
            # num 右移加在res上
            num = num >> 1
        return res

if __name__ == "__main__":
    rb = ReverseBits()
    num = 10
    print("二进制数 {} 翻转二进制后为: {}".format(num, rb.Solution(num)))


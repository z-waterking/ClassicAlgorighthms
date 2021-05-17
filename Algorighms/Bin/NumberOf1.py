# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   NumberOf1.py
@USER       :   ZZZZZ
@TIME       :   2021/5/17 17:47
'''

class NumberOf1():
    def __init__(self):
        pass

    def Solution(self, num):
        '''
        求num的二进制表示中1的个数
        :param num: 输入数字
        :return: 1的个数
        '''
        # n & n-1 会将n的二进制表示的最后一位变为0
        # (n)1110101 & (n-1)1110100 = 1110100
        res = 0

        while num != 0:

            print(bin(num))

            res += 1
            num = num & (num - 1)


        return res

if __name__ == "__main__":
    no = NumberOf1()
    num = 100
    print("二进制数 {} 中1的个数为: {}".format(num, no.Solution(num)))

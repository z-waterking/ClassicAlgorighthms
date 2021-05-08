# -*- coding: utf-8 -*-#
'''
@Project    :   ClassicAlgorighthms
@File       :   test.py
@USER       :   ZZZZZ
@TIME       :   2021/5/7 16:48
'''

res = []
def permute(nums):
    bc(nums, [])
    return res


def bc(nums, track):
    if len(track) == len(nums):
        res.append(track)
        return

    for i in range(len(nums)):
        if nums[i] in track:
            continue

        track.append(nums[i])
        bc(nums, track)
        track.pop()

print(permute([1, 2, 3]))
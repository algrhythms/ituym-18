"""
    Created by mbenlioglu on 1/20/2018
"""


def can_reachable(nums):
    x, y = nums
    i = 1
    while True:
        lvl = x * i
        if lvl <= y < lvl + i:
            print 'YES'
            break
        elif y < lvl:
            print 'NO'
            break
        i *= 2


if __name__ == '__main__':
    inputs = (int(s) for s in raw_input().split())
    can_reachable(inputs)

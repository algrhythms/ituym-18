"""
author: mertkosan
createdAt: 1/20/2018
"""
import math

n, a, b = (int(_input) for _input in raw_input().split(" "))

least = int(math.log(n, 2)) + 1
least = b if b < least else least
most = b

matrix = [[None for x in range(n + 1)] for y in range(most)]


def bst(h, n):
    global matrix
    if h < 0 or n < 0:
        return 0
    if matrix[h][n]:
        return matrix[h][n]
    if h == 0 and n == 0:
        matrix[h][n] = 1
        return 1
    elif h == 0 and n == 1:
        matrix[h][n] = 1
        return 1
    elif h == 0 and n > 1:
        matrix[h][n] = 0
        return 0
    elif h > 0 and n == 0:
        matrix[h][n] = 1
        return 1
    else:
        sum = 0
        for i in range(1, n + 1):
            sum += bst(h - 1, i - 1) * bst(h - 1, n - i)
        matrix[h][n] = sum
        return sum


most_bst = bst(most - 1, n)
least_bst = bst(least - 2, n)
total = most_bst - least_bst
print total

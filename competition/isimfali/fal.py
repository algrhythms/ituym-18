"""
author: mertkosan
createdAt: 1/20/2018
"""
import math


def permutation_rank(seq):
    ref = sorted(seq)
    if ref == seq:
        return 0
    else:
        rank = 0
        f = math.factorial(len(seq) - 1)
        for x in ref:
            if x < seq[0]:
                rank += f
            else:
                rank += permutation_rank(seq[1:]) if seq[1:] else 0
                return rank


def permute(seq, permutation):
    leng = len(permutation)
    result = [0] * leng
    for i, p in enumerate(permutation):
        result[p - 1] = seq[i]
    return result


def permute_n_times(seq, permutation, n):
    result = seq
    for j in range(n):
        result = permute(result, permutation)
    return result


q, leng, n_permute = (int(_input) for _input in raw_input().split(" "))
permutation = [int(_input) for _input in raw_input().split(" ")]
queries = []
for i in range(q):
    queries.append([int(_input) for _input in raw_input().split(" ")])

for query in queries:
    result = permute_n_times(query, permutation, n_permute)
    rank = permutation_rank(result)
    if rank % 2 == 0:
        print "NO"
    else:
        print "YES"

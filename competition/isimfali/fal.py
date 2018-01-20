"""
author: mertkosan
createdAt: 1/20/2018
"""
import math


def permutation_rank(seq):
    rank = 0
    ref = sorted(seq)
    newseq = seq
    while ref != newseq:
        f = math.factorial(len(seq) - 1)
        for x in ref:
            if x < seq[0]:
                rank += f
            else:
                del ref[ref.index(newseq[0])]
                del newseq[0]
    return rank


# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
#
# def lcm(a, b):
#     """Return lowest common multiple."""
#     return a * b // gcd(a, b)
#
#
# def lcmm(*args):
#     """Return lcm of args."""
#     return reduce(lcm, args)
#
#
# def find_permutation_cycle(perm):
#     visited = [False] * len(perm)
#     cycles = []
#     for j in xrange(len(visited)):
#         k = j
#         cnt = 0
#         while not visited[k]:
#             visited[k] = True
#             cnt = cnt + 1
#             k = perm[k] - 1
#         if cnt > 0:
#             cycles.append(cnt)
#     return lcmm(*cycles)


def permute(seq, permutation):
    leng = len(permutation)
    result = [0] * leng
    for i, p in enumerate(permutation):
        result[p - 1] = seq[i]
    return result


def permute_n_times(seq, permutation, n):
    # n = n % find_permutation_cycle(permutation)
    result = seq
    for j in range(n):
        result = permute(result, permutation)
    return result


q, leng, n_permute = (int(_input) for _input in raw_input().split())
permutation = [int(_input) for _input in raw_input().split()]
queries = []
for i in range(q):
    queries.append([int(_input) for _input in raw_input().split()])

for query in queries:
    result = permute_n_times(query, permutation, n_permute)
    rank = permutation_rank(result)
    if rank % 2 == 0:
        print "NO"
    else:
        print "YES"

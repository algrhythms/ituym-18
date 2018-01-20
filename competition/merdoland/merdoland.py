"""
author: mertkosan
createdAt: 1/20/2018
"""
from collections import deque

N, K = (int(_input) for _input in raw_input().split(" "))
paths = {}
for i in range(1, N + 1):
    paths[i] = []
for _ in range(1, N):
    a, b = (int(_input) for _input in raw_input().split(" "))
    paths.get(a).append(b)
    paths.get(b).append(a)

result = [0] * K
result[0] = N
result[K-1] = 1

queue = deque()
for i in range(1, N + 1):
    visited = set()
    visited.add(i)
    queue.append((i, 0))
    while queue:
        elm = queue.popleft()
        children = paths.get(elm[0])
        path_len = elm[1] + 1
        for child in children:
            if child not in visited:
                visited.add(child)
                result[path_len] += 1
                if path_len < K:
                    queue.append((child, path_len))

print result

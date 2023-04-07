from collections import defaultdict
n = int(input())
k = int(input())

# graph = [[0] * n for _ in range(n)]
graph = defaultdict(list)
for i in range(k):
    ops = list(map(int, input().split()))
    if ops[0] == 1:
        _, u, v = ops
        graph[u].append(v)
        graph[v].append(u)
    else:
        _, v = ops
        print(*graph[v])

from collections import deque


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


v, e = map(int, input().split())
in_degree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    in_degree[v2] += 1

topology_sort()
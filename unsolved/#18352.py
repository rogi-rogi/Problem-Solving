from heapq import heappop, heappush
from math import inf
from sys import stdin
input = stdin.readline

def Dijkstra(v) :
    pq = []
    heappush(pq, (0, v))
    dist[v] = 0
    while pq :
        w, v = heappop(pq)
        if dist[v] < w : continue
        w += 1
        for nv in graph[v] :
            if w < dist[nv] :
                dist[nv] = w
                heappush(pq, (w, nv))

if __name__ == "__main__" :
    N, M, K, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    dist = [inf] * (N + 1)
    for _ in range(M) :
        A, B = map(int, input().split())
        graph[A].append(B)
    Dijkstra(X)
    res = []
    for idx, d in enumerate(dist) :
        if d == K : res.append(idx)
    if res : print(*res, sep = '\n')
    else : print(-1)
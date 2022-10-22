# adjacency list ver
from collections import deque

def dfs(v) :
    path.append(v)
    visited[v] = True
    for nv in graph[v] :
        if not visited[nv] :
            dfs(nv)
            
def bfs(v) :
    queue = deque([v])
    visited[v] = True
    path.append(v)
    while queue :
        v = queue.popleft()
        for nv in graph[v] :
            if not visited[nv] :
                path.append(nv)
                queue.append(nv)
                visited[nv] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M) : 
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for i in range(1, N + 1) :
    graph[i].sort()
path, visited = [], [False] * (N + 1)
dfs(V)
print(*path)
path, visited = [], [False] * (N + 1)
bfs(V)
print(*path)

'''
# adjacency matrix ver
from collections import deque

def dfs(v) :
    path.append(v)
    visited[v] = True
    for nv in range(1, N + 1) :
        if not visited[nv] and graph[v][nv] :
            dfs(nv)
            
def bfs(v) :
    queue = deque([v])
    visited[v] = True
    path.append(v)
    while queue :
        v = queue.popleft()
        for nv in range(1, N + 1) :
            if not visited[nv] and graph[v][nv]:
                visited[nv] = True
                path.append(nv)
                queue.append(nv)

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M) : 
    v1, v2 = map(int, input().split())
    graph[v1][v2] = graph[v2][v1] = 1
    
path, visited = [], [False] * (N + 1)
dfs(V)
print(*path)
path, visited = [], [False] * (N + 1)
bfs(V)
print(*path)
'''

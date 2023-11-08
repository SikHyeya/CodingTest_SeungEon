# 23.11.08
# DFS와 BFS

# PyPy3로 제출했을 때 시간과 메모리가 더 많이 들었다.
import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True  # 방문 처리
    if visited[v]:
        dfs_list.append(v)

    for i in graph[v]:
        if not visited[i]: # 방문 안 한 노드이면
            dfs(graph, i, visited)  # 재귀

def bfs(graph, v, visited):
    visited = [False] * (n+1)   # bfs의 방문 여부가 저장된 리스트
    visited[v] = True  # 방문 처리
    queue = deque([v])  # 큐 생성 후, 시작 정점 삽입

    while queue:
        v = queue.popleft()
        bfs_list.append(v)
        for i in graph[v]:  # 인접 노드 중
            if not visited[i]: # 방문 안 한 노드이면
                visited[i] = True   # 방문 처리
                queue.append(i) # 큐에 추가


input = sys.stdin.readline
n, m, v = map(int, input().split()) # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(n+1)]    # 리스트의 0번째 인덱스는 무시하기 위해 n+1 칸 만들기 
visited = [False] * (n+1) # dfs의 방문 여부가 저장된 리스트
dfs_list = []
bfs_list = []   

# m개의 연결된 간선 정보 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순으로 인접 노드 방문하기 위해 정렬
for i in range(n+1):
    graph[i].sort()

dfs(graph, v, visited)
bfs(graph, v, visited)
print(*dfs_list)
print(*bfs_list)


# 다른 사람의 풀이 - 내 코드보다 빠름
"""
내가 더 익숙한 변수로 정리했다.
내가 작성한 코드와 동일하지만 변수를 더 최적화했고,
deque 대신 queue 사용(실행 결과 그냥 queue 사용이 더 빠르다. 뭐지?)
"""
import sys

input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    dfs_list.append(v)
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(i)

def bfs(v):
    visited[v] = True
    queue = [v]
    while queue:
        v = queue.pop(0)
        bfs_list.append(v)
        for i in sorted(graph[v]):
            if not visited[i]:
                visited[i] = True
                queue.append(i)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_list = []
bfs_list = []

dfs(V)
visited = [False] * (N + 1) # 초기화
bfs(V)

print(*dfs_list)
print(*bfs_list)
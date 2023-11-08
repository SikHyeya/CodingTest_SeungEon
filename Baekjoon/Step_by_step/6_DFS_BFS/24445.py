# 23.11.08
# 알고리즘 수업 - 너비 우선 탐색 2

# Python3(시간 더), PyPy3(메모리 더) 모두 통과.
import sys
from collections import deque

def bfs(graph, v, visited):
    global count
    visited[v] = count  # 방문하면 순서 나타내기
    queue = deque([v])  # 큐 생성 후, 시작 정점 삽입

    while queue:
        v = queue.popleft()
        for i in graph[v]:  # 인접 노드 중
            if visited[i] == 0: # 방문 안 한 노드이면
                count += 1
                visited[i] = count
                queue.append(i) # 큐에 추가


input = sys.stdin.readline
n, m, r = map(int, input().split()) # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(n+1)]    # 리스트의 0번째 인덱스는 무시하기 위해 n+1 칸 만들기 
visited = [0] * (n+1) # 방문 순서가 저장된 리스트. 0이면 방문 x
count = 1   # 방문 순서 카운팅 시 필요한 변수

# m개의 연결된 간선 정보 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 내림차순으로 인접 노드 방문하기 위해 정렬
for i in range(n+1):
    graph[i].sort(reverse=True)

bfs(graph, r, visited)

# 방문 순서 출력
for i in range(1, n+1):
    print(visited[i])
# 23.11.08
# 알고리즘 수업 - 너비 우선 탐색 1
"""
너비 우선 탐색 의사 코드
bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    for each v ∈ V - {R}
        visited[v] <- NO;
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    while (Q ≠ ∅) {
        u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
        for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
            if (visited[v] = NO) then {
                visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
                enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
            }
    }
}
"""

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
# print(graph)

# 오름차순으로 인접 노드 방문하기 위해 정렬
for i in range(n+1):
    graph[i].sort()
# print(graph)

bfs(graph, r, visited)

# 방문 순서 출력
for i in range(1, n+1):
    print(visited[i])
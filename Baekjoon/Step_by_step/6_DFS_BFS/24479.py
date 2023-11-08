# 23.11.08
# 알고리즘 수업 - 깊이 우선 탐색 1
"""
깊이 우선 탐색 의사 코드
dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
"""

# Python3 로는 통과, PyPy3로는 메모리 초과.
import sys

"""
아래 함수(Python이 정한 최대 재귀 깊이를 변경해주는 함수)가 없다면 RecursionError.
Python이 정한 최대 재귀 깊이는 sys.getrecursionlimit()로 확인 가능. 
BOJ의 채점 서버에서 이 값은 1,000으로 되어 있다.
"""
sys.setrecursionlimit(10 ** 6)  # 10의 6제곱

def dfs(graph, v, visited):
    global c
    visited[v] = c  # 방문하면 순서 나타내기

    for i in graph[v]:
        if visited[i] == 0: # 방문 안 한 노드이면
            c += 1
            dfs(graph, i, visited)  # 재귀

input = sys.stdin.readline
n, m, r = map(int, input().split()) # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(n+1)]    # 리스트의 0번째 인덱스는 무시하기 위해 n+1칸 만들기 
visited = [0] * (n+1) # 방문 순서 저장. 0이면 방문 x
c = 1

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

dfs(graph, r, visited)

# 방문 순서 출력
for i in range(1, n+1):
    print(visited[i])
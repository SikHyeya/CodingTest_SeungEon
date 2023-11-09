# 23.11.09
# 유기농 배추

# DFS 풀이
import sys

sys.setrecursionlimit(10 ** 6)  # 10의 6제곱

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    result = 0
    m, n, k = map(int, input().split()) # 가로길이, 세로길이, 간선의 수
    graph = [[0 for j in range(n)] for i in range(m)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    # print(graph)
    for i in range(m):
        for j in range(n):
            # 현재 위치에서 dfs 수행
            if dfs(i, j) == True:
                result += 1
    print(result)


# 다른 사람의 풀이 (BFS)
# 구조는 DFS와 동일하지만 조금 더 빠르다.
import sys

t = int(sys.stdin.readline())
row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

def bfs(x, y) :
    queue = [(x, y)]
    graph[x][y] = 0 
    
    while queue :
        x, y = queue.pop(0)
        for i in range(4) :
            nx = x + row[i]
            ny = y + col[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if graph[nx][ny] == 1 :
                queue.append((nx,ny))
                graph[nx][ny] = 0

for i in range(t) :
    n, m, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for i in range(n)]
    count = 0
    for i in range(k) :
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1
    for j in range(n) :
        for k in range(m) :
            if graph[j][k] == 1:
                bfs(j, k)
                count += 1
    print(count)
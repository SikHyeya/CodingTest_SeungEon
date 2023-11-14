# 23.11.14
# 토마토 - 3차원

# BFS
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        z, x, y= queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 범위 벗어나면 무시
            if nx < 0 or ny < 0 or nz <0 or nx >= n or ny >= m or nz >= h:
                continue
            # 토마토가 없으면 무시
            if graph[nz][nx][ny] == -1:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append([nz, nx, ny])

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append([i, j, k])
bfs()
res = 0
for gra in graph:
    for gr in gra:
        for g in gr:
            # 다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
            if g == 0:
                print(-1)
                exit(0)
            # 다 익혔다면 최댓값이 정답
            res = max(res, max(gr))
# 처음 시작을 1로 표현했으니 1을 빼준다.
print(res-1)
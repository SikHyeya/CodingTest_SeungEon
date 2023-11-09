# 23.11.09
# 나이트의 이동

# BFS
import sys
from collections import deque

dx = [-1, 1, -1, 1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

def bfs():
    queue = deque()
    queue.append((startX,startY))   # 시작 좌표
    while queue:
        x, y = queue.popleft()
        if x == endX and y == endY:
            return graph[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    l = int(input())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    graph = [[0] * l for _ in range(l)]
    graph[startX][startY] = 1
    print(bfs())

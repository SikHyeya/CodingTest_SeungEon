# 23.11.08
# 단지번호붙이기

"""
두 풀이 모두 PyPy3로 제출했을 때 시간과 메모리가 더 많이 들었다.
실행 결과 DFS가 조금 더 효율적.
"""

# DFS 풀이
# 이코테의 음료수 얼려먹기 문제를 참고해서 풀었다.
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global count
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        count +=1
        # 상 하 좌 우 위치 모두 재귀적으로 호출
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        # dfs(x - 1, y)
        # dfs(x, y - 1)
        # dfs(x + 1, y)
        # dfs(x, y + 1)
        return True
    return False

count = 0
result = 0
count_list = []
for i in range(n):
    for j in range(n):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            count_list.append(count)
            result += 1
            count = 0
print(result)

count_list.sort()
for i in range(len(count_list)):
    print(count_list[i])


# BFS 풀이
from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 0     # 방문 처리
    count = 1
        
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0     # 방문 처리
                queue.append([nx, ny])
                count += 1
    return count

result = 0
count_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count_list.append(bfs(i, j))
            result += 1
print(result)

count_list.sort()
for i in range(len(count_list)):
    print(count_list[i])
# 23.11.08
# 바이러스

"""
- 두 풀이 모두 오히려 PyPy3로 제출했을 때 시간과 메모리가 더 많이 들었다.
- DFS 풀이에서, 컴퓨터의 수는 100이하라 했으므로 Recursion 초과가 나지 않을 것 같아서
sys.setrecursionlimit() 함수를 사용하지 않았다.
"""
# DFS 풀이
import sys

def dfs(graph, v, visited):
    global count
    visited[v] = count

    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(graph, i, visited)

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]    # 리스트의 0번째 인덱스는 무시하기 위해 n+1 칸 만들기 
visited = [0] * (n+1) # 방문 순서 저장. 0이면 방문 x
count = 1

# m개의 연결된 간선 정보 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(graph, 1, visited)

# 정답 출력
print(count-1)


# BFS 풀이
import sys
from collections import deque

def bfs(graph, v, visited):
    global count
    visited[v] = count
    queue = deque([v])  # 큐 생성 후, 시작 정점 삽입

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                count += 1
                visited[i] = count
                queue.append(i) # 큐에 추가

input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]    # 리스트의 0번째 인덱스는 무시하기 위해 n+1 칸 만들기 
visited = [0] * (n+1) # 방문 순서 저장. 0이면 방문 x
count = 1

# m개의 연결된 간선 정보 입력받기
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, visited)

# 정답 출력
print(count-1)


# 다른 사람의 풀이 - 오호..
import sys

input = sys.stdin.readline
a = int(input())
b = int(input())
b_lst = []

result = set()
for i in range(b) :
    num = list(map(int,input().split()))
    if 1 in num :
        result.add(num[0])
        result.add(num[1])
    else :
        b_lst.append(num)
    
while True :
    for i in b_lst :
        if i[0] in result :
            result.add(i[1])
            b_lst.remove(i)
            break
        elif i[1] in result :
            result.add(i[0])
            b_lst.remove(i)
            break
    else :
        break

print(len(result) - 1 )
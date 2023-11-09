# 23.11.09
# 숨바꼭질

# BFS
from collections import deque

n, k = map(int, input().split())

def bfs():
    queue = deque()
    queue.append(n) # queue = deque([5])

    while queue:
        x = queue.popleft() # 처음 시작점은 x = 5, q = deque([]))
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x+1, x*2):  # nx = 4, 6, 10
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)

MAX = 10 ** 5   # 시간 초과 안 나도록하는 변수
dist = [0] * (MAX+1)    # 이동하는 거리를 저장하는 리스트
bfs()


# 다른 사람의 풀이
import sys

def f(n,k):
  if n>=k:return n-k
  if k==1:return 1
  if k%2:return min(f(n,k+1),f(n,k-1))+1     
  return min(k-n,f(n,k//2)+1)
print(f(*map(int,sys.stdin.readline().split())))
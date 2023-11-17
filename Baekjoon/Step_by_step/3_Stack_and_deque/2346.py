# 23.11.17
# 풍선 터뜨리기

# 풀이 1
from collections import deque
n = int(input())
queue = deque(enumerate(map(int, input().split())))
answer = []

index, value = queue.popleft()
answer.append(index+1)

for _ in range(n-1):
    if value > 0:
        for _ in range(value - 1):
            a = queue.popleft()
            queue.append(a)
    else:
        for _ in range(-value):
            a = queue.pop()
            queue.appendleft(a)

    index, value = queue.popleft()
    answer.append(index+1)

print(*answer)

# 풀이 2
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, ans)))
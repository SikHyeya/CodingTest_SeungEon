# 23.11.05
# 카드 2

from collections import deque

n = int(input())
queue = deque([_ for _ in range(1, n+1)])

while len(queue) != 1:
    queue.popleft()
    a = queue.popleft()
    queue.append(a)
print(queue.popleft())
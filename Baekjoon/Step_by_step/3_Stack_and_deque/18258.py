# 23.11.05
# 큐 2

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
queue = deque()

for _ in range(n):
    command = input().rstrip()

    if "push" in command:
        queue.append(int(command[5:]))
    elif "pop" in command:
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif "size" in command:
        print(len(queue))
    elif "empty" in command:
        if not queue:
            print(1)
        else:
            print(0)
    elif "front" in command:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif "back" in command:
        if not queue:
            print(-1)
        else:
            print(queue[-1])

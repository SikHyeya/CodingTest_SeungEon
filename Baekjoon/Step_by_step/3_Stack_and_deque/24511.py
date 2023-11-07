# 23.11.05
# queuestack

# 시간 초과 - 잘못된 풀이
from collections import deque

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

zipped_list = list(map(list, zip(a, b)))

answer = []
for c_val in c:
    for zipped in zipped_list:
        if zipped[0] == 0: # 큐면
            zipped.append(c_val)
            c_val = zipped.pop(1)
        else:
            continue
    answer.append(c_val)
print(*answer)


# 다른 사람의 풀이
import sys
from collections import deque

n = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))  # 0 1 1 0 (0 = queue, 1 = stack)
list_b = list(map(int, sys.stdin.readline().split()))  # 1 2 3 4

m = int(sys.stdin.readline())
list_c = list(map(int, sys.stdin.readline().split()))  # 2 4 7

res = deque()

for qs in range(n):
    if list_a[qs] == 0:
        res.appendleft(list_b[qs])  # 4 , 1
        
for i in range(m):
    res.append(list_c[i]) # 4, 1, 2, 4, 7
    print(res.popleft(), end=' ') # 4, 1, 2

# 23.11.05
# 제로

import sys

n = int(input())
input = sys.stdin.readline
stack = []

for _ in range(n):
    num = input().rstrip()
    
    if num == "0":
        stack.pop()
    else:
        stack.append(num)
print(sum(map(int, stack)))
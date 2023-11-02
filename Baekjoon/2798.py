# 23.11.02
# 블랙잭

from itertools import combinations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
result = []
a = list(combinations(numbers, 3))
for s in a:
    if sum(s) <= m:
        result.append(sum(s))
print(max(result))

# 다른 사람의 풀이
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
card=sorted(list(map(int,input().split())), reverse=True)
x=0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            num = card[i]+card[j]+card[k]
            if num <= m: 
                if x < num: x = num
                break

print(x)
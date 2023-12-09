# 23.12.09
# 학생회 뽑기

from itertools import combinations

n, k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse = True)

comb = list(combinations(a, k))
for i in comb:
    while i:
        a = bin
    
# 23.11.06
# N과 M (2)

# 조합
from itertools import combinations

n ,m = map(int, input().split())
print('\n'.join(list(map(' '.join, combinations(map(str, range(1, n+1)), m)))))

# 다른 사람의 풀이 - 백트래킹
N, M = map(int, input().split())
ans = []

def back(start):
    if len(ans) == M: # 배열의 길이를 확인
        print(" ".join(map(str, ans))) # 1 2 3 이런 상태로 출력하기 위해
        return 
    for i in range(start, N+1): # 1 ~ N 까지
        if i not in ans: # 중복 확인
            ans.append(i) # 배열 추가
            back(i+1) # 재귀
            ans.pop() # return으로 돌아오면 이게 실행됨. 1, 2, 3 일때 3을 없앰으로 전 단계로 돌아가는 것
            
back(1)
# 23.11.06
# N-Queen

# python으로는 시간초과를 피할 수 없음 => pypy3로 제출해야 통과됨

# 같은 행, 열, 대각선에는 다른 퀸을 놓을 수 없음
n = int(intput())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)

# 이 코드로 통과
import sys

input = sys.stdin.readline

n = int(input())

def promising(row):
    for before_row in range(row):
        # 같은 열 or 같은 대각선 상에 있는 경우
        if(graph_col[before_row] == graph_col[row] or 
           abs(graph_col[before_row]-graph_col[row])==abs(before_row-row)):
            return False
    return True

result = 0
graph_col = [0] * n 

def dfs(row):
    global result
    if row == n:
        result += 1
    else:
        for i in range(n):
            # Queen 놓기
            graph_col[row] = i
            if promising(row):
                dfs(row+1)

dfs(0)
print(result)

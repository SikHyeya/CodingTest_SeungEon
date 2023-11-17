# 23.11.15
# 체스판 다시 칠하기


"""
이 문제는 이해하기가 어려워서 다른 사람의 코드를 참고헸다.
"""
n, m=map(int,input().split())

graph=[]
cnt=[]
for i in range(n):
    graph.append(input())

"""
9*9 보드에서 자를 수 있는 경우의 수는, 2*2로 4가지이다.
10*10 보드에서 자를 수 있는 경우의 수는 3*3으로 9가지이다.
즉, N*M 보드에서 자를 수 있는 경우의 수는 N-i * M-j 가지가 된다.
"""    
for a in range(n-7):
    for b in range(m-7):    # 8 * 8로 자르기 위해, -7 해준다.
        w_index = 0   # 흰색으로 시작하는 경우
        b_index = 0   # 검은색으로 시작하는 경우
        for i in range(a, a + 8):   # 시작지점
            for j in range(b, b + 8):  # 시작지점
                if (i + j) % 2 == 0:    # 짝수인 경우
                    if graph[i][j] != 'W':    # W가 아니면, 즉 B이면
                        w_index += 1#W로 칠하는 갯수
                    else:   # W일 때
                        b_index += 1    # B로 칠하는 갯수
                else:   # 홀수인 경우
                    if graph[i][j] != 'W':  # W가 아니면, 즉 B이면
                        b_index += 1    # B로 칠하는 갯수
                    else:
                        w_index += 1    # W로 칠하는 갯수
                        
        cnt.append(w_index) # W로 시작할 때 경우의 수
        cnt.append(b_index) # B로 시작할 때 경우의 수
print(min(cnt))
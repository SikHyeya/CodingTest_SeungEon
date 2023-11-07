# 23.11.07
# 스도쿠

# Python3로는 통과 안 됨.
# PyPy3로만 통과.

import sys

# x행에서 n값(스도쿠의 실제 값)이 중복되는지 확인
def checkRow(x, n):
    for i in range(9):
        if n == graph[x][i]:
            return False    # 중복이면
    return True             # 중복이 아니면 = 유망

# y열에서 n값(스도쿠의 실제 값)이 중복되는지 확인
def checkCol(y, n):
    for i in range(9):
        if n == graph[i][y]:
            return False
    return True

# 3 * 3 영역에서 n값이 중복되는지 확인
def checkRect(x, y, n):
    # (x, y)가 속한 3 * 3 영역의 왼쪽 상단 좌표 (사각형의 제일 처음 좌표)
    nx = x // 3 * 3
    ny = y // 3 * 3
    # (x, y)좌표가 속한 3 * 3 영역 확인
    for i in range(3):
        for j in range(3):
            if n == graph[nx+i][ny+j]:
                return False
    return True

# 백트래킹 함수
def backTracking(n):
    # 스도쿠의 빈 칸을 모두 채웠다면
    # 정답이면 출력
    if n == len(blank):
        for _ in range(9):
            print(*graph[_])    # 정답 출력
        exit(0)                 # 프로그램 종료
    
    # 반복문을 통해 빈 칸에 1부터 9까지 넣어본다.
    # 정답이 아니면 모든 자식노드에 대해서
    for i in range(1, 10):
        x = blank[n][0] # 빈 칸의 x좌표
        y = blank[n][1] # 빈 칸의 y좌표

        # 유망한지 확인
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            graph[x][y] = i     # 스도쿠 값 채워주기 / 자식노드로 이동
            backTracking(n + 1) # 다음 빈 칸으로 이동 / 백트래킹 재귀
            graph[x][y] = 0     # 백트래킹을 위해 현재 위치 초기화 = 다시 빈칸으로 만듬 / 부모 노드로 이동
                                # 이 숫자를 사용한 경우의 탐색이 끝나면 해당 위치를 다시 빈 칸으로 만들어야 다음 경우의 탐색이 가능
    

graph = []  # 스도쿠 값 배열
blank = []  # 스도쿠의 빈 칸 위치 좌표를 담고있는 2차원 배열
for i in range(9):
    # 처음 입력 받기
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(9):
        if graph[i][j] == 0:
            blank.append([i, j])    # 스도쿠 빈 칸 위치

backTracking(0)
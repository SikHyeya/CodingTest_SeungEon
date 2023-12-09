# 23.12.09
# 개구리 매칭

# 주호 현재 위치, 개구리 수
s, n = map(int, input().split())
# 개구리 위치
e = list(map(int, input().split()))
# 점프 범위, 체력 소모량
k , l = map(int, input().split())

answer = []
for i in range(len(e)) :
    d = abs(s-e[i])
    if k * 2 >= d:
        a = k * 2 - d
    else:
        a = (d - (k * 2)) * l
    answer.append([a,i])

print(min(answer)[0], min(answer)[1]+1)
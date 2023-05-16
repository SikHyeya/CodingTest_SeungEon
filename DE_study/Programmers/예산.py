# 예산
# Lv.1
# https://school.programmers.co.kr/learn/courses/30/lessons/12982

# solution1
def solution1(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break
    return answer

# solution2
def solution2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)
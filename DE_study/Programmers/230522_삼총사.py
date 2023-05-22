# 삼총사
# Lv.1
# https://school.programmers.co.kr/learn/courses/30/lessons/131705

# 내 풀이
from itertools import combinations
def solution1(number):
    answer = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            answer += 1
    return answer

# 다른 사람의 풀이
def solution2(number):
    answer = 0
    for i in range(0,len(number)-2):
        for j in range(i+1,len(number)-1):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer

"""
<ChatGPT에게 물어보기>
Q. 아래 두 함수 중에 어떤게 더 최적화되어 있고, 효율적이야?

A. 두 함수 중에서는 solution1 함수가 더 최적화되어 있고 효율적입니다.
solution1 함수는 itertools 모듈의 combinations 함수를 사용하여 주어진 리스트 number에서 중복되지 않는 3개의 요소 조합을 생성합니다. 
각 조합의 합이 0인지 확인하고, 0이라면 결과값 answer를 증가시킵니다. 
이 함수의 시간 복잡도는 O(n^3)입니다. 
combinations 함수를 사용하여 가능한 모든 3개의 요소 조합을 생성하므로 O(n^3)의 시간이 소요됩니다.

solution2 함수는 3개의 반복문을 사용하여 number 리스트에서 모든 3개의 요소 조합을 생성합니다. 
각 조합의 합이 0인지 확인하고, 0이라면 결과값 answer를 증가시킵니다. 
이 함수의 시간 복잡도는 O(n^3)입니다. 
세 개의 반복문을 사용하여 모든 3개의 요소 조합을 생성하므로 O(n^3)의 시간이 소요됩니다.
두 함수의 시간 복잡도는 동일하나, solution1 함수는 itertools 모듈의 combinations 함수를 사용하여 코드가 간결해졌으며, 
중복되지 않는 조합을 생성하기 때문에 조합의 수가 줄어들어 효율적입니다. 
따라서, solution1 함수가 더 최적화되어 있고 효율적입니다.
"""
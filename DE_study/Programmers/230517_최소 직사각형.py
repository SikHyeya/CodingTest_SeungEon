# 최소 직사각형
# Lv.1
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

# 내 풀이
def solution1(sizes):
    w = []
    h = []
    for size in sizes:
        size.sort()
        w.append(size[0])
        h.append(size[1])
    return max(w) * max(h)

#다른 사람의 풀이
def solution2(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col

"""
<ChatGPT에게 물어보기>
Q. 아래 두 함수 중에 어떤게 더 최적화되어 있고, 효율적이야?

A. 두 함수 중에서는 solution2 함수가 더 최적화되어 있고 효율적입니다.
solution1 함수는 sizes 리스트를 반복하면서 각 요소를 정렬한 후 가로와 세로 값을 따로 저장합니다. 
그리고 저장된 가로와 세로 값 중 최대값을 곱해서 결과를 반환합니다. 
이 함수의 시간 복잡도는 O(nlogn)입니다. 
각 요소를 정렬하기 위해 O(logn)의 시간이 들고, 모든 요소를 반복하기 때문에 O(n)의 시간이 추가로 듭니다.

solution2 함수는 가로와 세로 값을 따로 저장하는 대신, 반복문에서 바로 가로와 세로 값을 비교하고 최대값을 갱신합니다. 
이렇게 하면 정렬하는 과정이 없기 때문에 더 효율적입니다. 
이 함수의 시간 복잡도는 O(n)입니다. 
sizes 리스트의 요소 수에 비례하여 단일 반복문을 수행하므로 선형 시간이 소요됩니다.
따라서, solution2 함수가 더 최적화되어 있고 효율적입니다.
"""
# 23.12.09
# 겹다각형의 각

"""
다각형이 하나일 때는 다각형의 내각의 합 공식.
여러 개 일때는 내부에 있는 다각형의 꼭짓점이 바깥의 다각형에 변 위에 놓이는 경우이므로,
제일 바깥 다각형의 내각의 합 + 나머지 다각형의 꼭짓점 수 * 180
"""

n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(180 * (int(*a) - 2))
else:
    print(180 * (int(a[0]) - 2) + 180 * sum(a[1:]))
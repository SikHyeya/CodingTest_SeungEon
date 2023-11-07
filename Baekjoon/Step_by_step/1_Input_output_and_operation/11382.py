# 23.11.01
# 꼬마 정민

a, b, c = map(int, input().split())
print(a + b + c)

# 다른 사람의 풀이
# 이렇게 하면 입력이 3개가 넘어도 오류가 나지 않기 때문에 별로인듯
print(sum(map(int, input().split())))
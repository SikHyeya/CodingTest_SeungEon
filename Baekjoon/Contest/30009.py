# 23.12.09
# 포지션 제로

# 리스트 사용
n = int(input())
x, y, r = map(int, input().split())
p = []
boundary = 0
count = 0
for i in range(x-r, x+r+1):
    p.append(i)
for _ in range(n):
    t = int(input())
    if t == p[0] or t == p[-1]:
        boundary += 1
    elif t in p:
        count += 1
print(count, boundary)

# 리스트 사용 x
n = int(input())
x, y, r = map(int, input().split())
boundary = 0
count = 0
left_boundary = x - r
right_boundary = x + r
for _ in range(n):
    t = int(input())
    if t == left_boundary or t == right_boundary:
        boundary += 1
    elif left_boundary < t < right_boundary:
        count += 1
print(count, boundary)
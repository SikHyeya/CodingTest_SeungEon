# 23.11.13
# 영화감독 숌

"""
문제가 이해가 안 돼서 구글링해서 풀었다.
1666, 2666, ... 5666, (6666이 아니라)6660이다.(6660이 666을 포함하고 있는 숫자로서 6666보다 작기 때문)
"""
n = int(input())
number = 666    # 666부터 시작
count = 0       # 666이 포함될 때만 카운트 하기 위함
while True:
    if "666" in str(number):
        count += 1
        if count == n:  # 정답일 때
            print(number)
            break
    number += 1

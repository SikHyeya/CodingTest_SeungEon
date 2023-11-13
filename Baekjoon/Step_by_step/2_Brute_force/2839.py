# 23.11.13
# 설탕 배달

n = int(input())
count = 0
while n >= 0:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)
        
# 다른 사람의 풀이
# 경우의 수는 총 4가지이므로 조건문을 사용하여 풀이
n = int(input())

if n % 5 == 0:  # 5으로 나눠떨어질 때
    print(n // 5)
else:
    p = 0
    while n > 0:
        n -= 3
        p += 1
        if n % 5 == 0:  # 3kg과 5kg를 조합해서 담을 수 있을 때
            p += n // 5
            print(p)
            break
        elif n == 1 or n == 2:  # 설탕 봉지만으로 나눌 수 없을 때
            print(-1)
            break
        elif n == 0:  # 3으로 나눠떨어질 때
            print(p)
            break
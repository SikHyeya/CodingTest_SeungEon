# 23.11.07
# 알고리즘 수업 - 피보나치 수 1

# 재귀 호출 의사 코드
"""
fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}
"""
# 동적 프로그래밍 의사 코드
"""
fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
"""

# Python3로 하면 시간초과, PyPy3로 하면 통과
n = int(input())
count_1 = 0
count_2 = 0

def fib(n):
    global count_1
    if n == 1 or n == 2: 
        count_1 += 1 
        return 1    # 코드 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacci(n):
    global count_2  
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 1

    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]  # 코드 2
        count_2 += 1
    return f[n]

fib(n)
fibonacci(n)
print(count_1, count_2)
 

# 다른 사람의 코드 1 - ㅋㅋ
n = int(input())
f = [0, 1, 1]
for i in range(3, n+1):
    f.append(f[-1] + f[-2])
print(f[n], n-2)

# 다른 사람의 코드 2 - Swap 하는 방식
from sys import stdin

n = int(stdin.readline())
a = 1
b = 2
for _ in range(3, n):
    a, b = b, a + b
print(b, n - 2)
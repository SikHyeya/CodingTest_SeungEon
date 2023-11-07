# 23.11.01
# 곱셈

a = int(input())
b = list(map(int, input()))

i, j, k = [a * b[-i] for i in range(1, 4)]
print(i, j, k, i + j * 10 + k * 100, sep="\n")

# 다른 사람의 풀이 1
a, b = int(input()), input()    # a는 정수형으로 입력받고, b는 문자형으로 입력받는다.
# 별표(*)는 리스트의 요소를 풀어낼 때 사용
print(*[a * int(i) for i in b][::-1], a * int(b), sep="\n")     # (줄 바꿈 안 해도 통과 됨) 

# 다른 사람의 풀이 2
# 이 풀이를 처음에 떠올렸는데 왜 저렇게 풀었지
a, b = int(input()), input()
for p in b[::-1]:
    print(a * int(p))
print(a * int(b))
    


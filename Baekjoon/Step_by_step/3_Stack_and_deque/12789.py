# 23.11.05
# 도키도키 간식드리미

n = int(input())
people = list(map(int, input().split()))
stack = []
target = 1

for i in people:
    stack.append(i)
    while stack and stack[-1] == target:
        stack.pop()
        target += 1
    if len(stack) > 1 and stack[-1] > stack[-2] :
        break

if stack:
    print("Sad")
else:
    print("Nice")


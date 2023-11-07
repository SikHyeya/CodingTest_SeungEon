# 23.11.05
# 괄호

n = int(input())

for _ in range(n):
    stack = []
    vps = input()

    for i in vps:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                stack.append(i)
                break
            else:
                stack.pop()

    if stack:
        print("NO")
    else:
        print("YES")
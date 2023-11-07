# 23.11.05
# 균형잡힌 세상

while True:
    text = input()
    stack = []

    # ??
    if text == ".":
        break

    for i in text:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
                break
    if stack:
        print("no")
    else:
        print("yes")
    

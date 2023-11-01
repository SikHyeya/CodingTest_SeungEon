# 입력 받기
n = int(input())
words = []
for i in range(n):
    words.append(input())

first = []

for word in words:
    for i in range(len(word)):
        if word[i] not in first:
            first.append(word[i])
            #word = word.replace(word[i], "["+word[i]+"]")
            print(word, "단어 "+word[i])
            break
        else:
            pass
print(first)

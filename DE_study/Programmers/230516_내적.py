# 내적 
# Lv.1
# https://school.programmers.co.kr/learn/courses/30/lessons/70128

# solution1
def solution1(a, b):
    return sum([i*j for i,j in zip(a,b)])

# solution2
def solution2(a, b):
    c =[]
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return sum(c)

#solution3
import numpy as np
def solution3(a, b):
    return int(np.dot(a, b)) 
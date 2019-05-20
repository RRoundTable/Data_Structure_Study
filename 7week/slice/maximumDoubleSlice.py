import time
import numpy as np
from itertools import combinations
import math
# Wrong answer: 더 많은 경우의 수가 있다.
def solution1(a):
    first = 0
    second = 0
    third = 0
    total_sum = sum(a)
    max_v = min(a)
    tmp_sum = total_sum
    for i, e in enumerate(a[:-2]):
        tmp_sum -= e
        if tmp_sum > max_v:
            max_v = tmp_sum
            first = i
    a = a[first+1: ] # slice
    a = list(reversed(a))
    total_sum = sum(a)
    tmp_sum = total_sum
    max_v = min(a)
    for i, e in enumerate(a[:-1]):
        tmp_sum -= e
        if tmp_sum > max_v:
            max_v = tmp_sum
            third = i
    a = a[third+1: ]
    min_v = min(a)
    return sum(a) - min_v

def solution2(a):
    first = 0
    second = 0
    third = 0
    total_sum = sum(a)
    max_v = min(a)
    tmp_sum = total_sum
    a = list(reversed(a))
    for i, e in enumerate(a[:-2]):
        tmp_sum -= e
        if tmp_sum > max_v:
            max_v = tmp_sum
            first = i
    a = a[first+1: ] # slice
    a = list(reversed(a))
    total_sum = sum(a)
    tmp_sum = total_sum
    max_v = min(a)
    for i, e in enumerate(a[:-1]):
        tmp_sum -= e
        if tmp_sum > max_v:
            max_v = tmp_sum
            third = i
    a = a[third+1: ]
    min_v = min(a)
    return sum(a) - min_v

def solution(a):
    a1 = solution1(a)
    a2 = solution2(a)
    print(a1, a2)
    if a2 > a1:
        answer = a2
    else:
        answer = a1
    return answer

def solution(a):
    idx = list(range(len(a)-1))
    combs = list(combinations(idx, 3))
    result = []
    for x, y, z in combs:
        result.append(sum(a[x+1:y]) + sum(a[y+1:z]))
    if len(result) == 0:
        return 0
    return max(result)

# dynamic programming
def solution(a):

    k1 = [0] * len(a)
    k2 = [0] * len(a)
    l = len(a)
    for i in range(1, l-1):
        k1[i] = max(k1[i-1] + a[i], 0)

    for i in reversed(range(1, l-1)):
        k2[i] = max(k2[i+1] + a[i], 0)
    max_v = 0
    print("k1: {}".format(k1))
    print("k2: {}".format(k2))
    for i in range(1,l-1):
        max_v = max(max_v, k1[i-1] + k2[i+1])
    return max_v

# test1: correctness
a = [3, 2, 6, -1, 4, 5, -1, 2]
expected = 17
print("1: {}".format(solution(a) == expected)) # 17

# test2: correctness error
a = [3, 2, -60, -1, 4, 5,-1, 2 ]
expected = 10
print("2: {}".format(solution(a) == expected)) # 0

# test3: correctness
a = [3, 2, 6, -1, 4, -5, -1, 2]
expected = 12
print("3: {}".format(solution(a) == expected)) # 12

# test4: correctness
a = [3, 2, 6 ]
expected = 0
print("4: {}".format(solution(a) == expected)) # 0


# test5: correctness
a = [3, 2, 6, 10000]
expected = 6
print("5: {}".format(solution(a) == expected)) # 6
print(solution(a))

# test7: correctness
a = [3, 2000, 6, 10000]
expected = 2000
print("6: {}".format(solution(a) == expected))# 2000


# test7: correctness
a = [0, 10, -5, -2, 0]
expected = 10
print("7: {}".format(solution(a) == expected)) # 2000


# test8: correctness
a = [-10000, -2000, -30, -30, -90]
expected = 0
print("8: {}".format(solution(a) == expected)) # 2000

# # test4
# a = np.random.randint(-10000, 10000, 100000)
# start = time.time()
# print(solution(a))
# end = time.time()
# print("time: {}".format(end - start))
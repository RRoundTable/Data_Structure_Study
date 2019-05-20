import time
import numpy as np
from itertools import combinations
import math
from bisect import bisect_left
def solution(a):
    dics = {}
    count = 0
    for i, e in enumerate(a[:-1]):
        max_value = i + e
        for j, e in enumerate(a[i+1:]):
            min_value = j - e + i + 1
            if max_value < min_value:
                continue
            else:
                count += 1
    return count

def solution(a):
    min_dict = [None] * len(a)
    max_dict = [None] * len(a)
    for i, e in enumerate(a):
        min_dict[i] = i - e
        max_dict[i] = i + e
    count = 0
    indexs = list(range(len(min_dict)))
    indexs = sorted(indexs, key=(lambda x: min_dict[x]))
    min_dict_t = sorted(min_dict)
    selected = []
    for i in range(len(a)-1):
        c = 0
        for t in min_dict_t:

            if t <= max_dict[i]:
                c += 1
                continue
            else:
                break
        count += c - (i + 1)
    return count

def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
            return midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return midpoint


def solution(a): # N long(N)

    A1 = [None] * len(a)
    A2 = [None] * len(a)
    for i, e in enumerate(a):
        A1[i] = i + e
        A2[i] = -1 * ( e - i)

    A1 = sorted(A1)
    A2 = sorted(A2)
    cnt = 0
    for i in reversed(range(len(a))):
        pos = bisect_left(A2, A1[i])
        if pos >= 0:
            while pos < len(a) and A2[pos] == A1[i]:
                pos += 1
            cnt += pos
        else: # element not there
            insertpoint = -(pos + 1)
            cnt += insertpoint
    l = len(a)
    sub = l * (l + 1) / 2.0
    cnt -= sub
    if cnt > 1e7:
        return -1
    return int(cnt)

# for문을 최소화하기
# test1: correctness
a = [1, 5, 2, 1, 4, 0]
print(solution(a))

# test2 : efficiency
a = list(range(10000))
start = time.time()
print(solution(a))
end = time.time()
print(end - start)

# test3: correctness
a = [1, 1, 2, 1, 4, 0]
print(solution(a))

# test4: correctness
a = [1, 6, 2, 1, 1, 0]
print(solution(a))

# test5 : efficiency
a = np.random.randint(0, 20000000, 100000)
a = list(a)
start = time.time()
print(solution(a))
end = time.time()
print(end - start)

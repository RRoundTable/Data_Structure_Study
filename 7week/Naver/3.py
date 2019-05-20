import time
import numpy as np
from itertools import combinations
from bisect import bisect_left

def unis(alist):
    alist = sorted(alist)
    unique_set = sorted(list(set(alist)))
    start = 0
    last = 0
    result = []

    for u in unique_set[1:]:

        idx = bisect_left(alist,u)

        result.append(idx - start)

        start = idx

    result.append(len(alist) - start)

    return result.count(1)


def solution(a):

    l = len(a)
    combs = []
    for i in range(l):
        for j in range(l - i):
            tmp = a[i : i + j + 1]
            combs.append(tmp)
    # for i in range(2, l+1):
    #
    #     combs += list(combinations(a, i))
    cnt = 0
    # combs = list(set(combs))
    for c in combs:
        print(c, unis(c))
        cnt += unis(c)
    return cnt


# test1: correctness
a = 'ACAX'
expected = [4, 6, 8]
print(solution(a) == expected)

# test2: correctness
a = [30, 20, 10]
expected = [0, 1, 2]
print(solution(a) == expected)  # 17


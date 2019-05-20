
import time
import math
from bisect import bisect_left

# time complexity: O(N*N)
def solution(a):
    unique_set = set(a)
    total = len(a)
    count = []
    for u in unique_set:
        cnt = a.count(u) # O(N)
        if cnt > round(total / 2.0):
            return u
        elif cnt == total/2:
            return -1
        count.append(cnt)
    idx = count.index(max(count))
    return unique_set[idx]

def solution(a):
    a = sorted(a) # O(NlogN)
    unique_set = sorted(set(a))
    unique_set_ = unique_set.copy()
    unique_set.pop(0)
    total_len = len(a)
    count = []
    base = 0
    for i, u in enumerate(unique_set):
        last = a.index(u)
        if last - base > int(total_len/2.0):
            return unique_set_[i]
        elif last - base == int(total_len/2.0):
            return -1
        count.append(last - base)
        base = last
    count.append(total_len - base)
    max_v = max(count)
    if count.count(max_v) > 1:
        return -1
    return unique_set_[count.index(max_v)]


def solution(a):
    if len(a) == 0: # empty array일때
        return -1
    original = a.copy()
    a = sorted(a) # O(NlogN)
    unique_set = sorted(set(a))
    unique_set_ = unique_set.copy()
    unique_set.pop(0)
    total_len = len(a)
    count = []
    base = 0
    for i, u in enumerate(unique_set):
        last = bisect_left(a, u)
        if last - base == total_len / 2 and total_len % 2 == 0:
            return -1
        count.append(last - base)
        base = last
    count.append(total_len - base)
    max_v = max(count)
    if max_v > int(total_len/2):
        idx = count.index(max_v)
        return original.index(unique_set_[idx])
    else:
        return -1

# test1: correctness
a = [3, 4, 3, 2, 3, -1, 3, 3] # 0
print(solution(a))

# test2: correctness
a = [4, 4, 3, 2, 3, -1, 3, 3] # -1
print(solution(a))

# test3: correctness
a = [4, 4, 4, 4, 3, 4, 3, 3] # 0
print(solution(a))

# test4: correctness
a = list(range(100000))
start = time.time()
print(solution(a))
end = time.time()
print("time: {}".format(end - start))

# test5: correctness
a = [4, 4, 4, 4, 3, 4, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5] # 0
print(solution(a))

# test7: correctness
a = [4, 4, 4, 4, 5,5,5,5,5] # 0
print(solution(a))
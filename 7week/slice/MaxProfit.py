import time
import math
import numpy as np

# dynamic programing: runtime error -> check non-empty condition
def solution(a):
    if len(a) == 0:
        return 0
    k1 = [0] * len(a)
    k1[0] = a[0]
    l = len(a)
    for i in range(1,l):
        k1[i] = min(k1[i-1], a[i])

    result = []
    for i in range(l):
        result.append(a[i] - k1[i])
    return max(result)

# test1
a = [23171, 21011, 21123, 21366, 21013, 21367]
expected = 356
print("1: {}".format(solution(a) == expected))

# test2
a = [23171, 21011, 0, 21366, 21013, 21367]
expected = 21367
print("2: {}".format(solution(a) == expected))

# test3
a = [23171, 21011, 30000, 21366, 21013, 21367]
expected = 30000 - 21011
print("3: {}".format(solution(a) == expected))

# test4
a = [23171, 21011]
expected = 0
print("4: {}".format(solution(a) == expected))

# test4
a = [23171]
expected = 0
print("4: {}".format(solution(a) == expected))

# test4
a = []
expected = 0
print("4: {}".format(solution(a) == expected))

# test6
a = list(np.random.randint(0, 200000, 40000))
expected = 0
start = time.time()
print("5: {}".format(solution(a) == expected))
end = time.time()
print("time: {}".format(end - start))
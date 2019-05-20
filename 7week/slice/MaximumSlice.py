import time
import math
import numpy as np

# dynamic programing: runtime error
def solution(a):
    l = len(a)
    k = [0] * l
    k[0] = a[0]
    for i in range(1, l):
        k[i] = max(k[i-1], 0) + a[i]
    return max(k)

# test1
a = [3, 2, -6, 4, 0]
expected = 5
print("1: {}".format(solution(a) == expected))

# test2
a = [3, 2, -6, 15, 0]
expected = 15
print("2: {}".format(solution(a) == expected))

# test3
a = [0, 0, 0, 0, 0]
expected = 0
print("3: {}".format(solution(a) == expected))

# test4
a = [1]
expected = 1
print("4: {}".format(solution(a) == expected))

# test5
a = [1]
expected = 1
print("5: {}".format(solution(a) == expected))

# test6
a = [10, 1, 2, 3, -100]
expected = 16
print("6: {}".format(solution(a) == expected))


# test6
a = list(np.random.randint(-1000000, 1000000, 1000000))
expected = 0
start = time.time()
print("5: {}".format(solution(a) == expected))
end = time.time()
print("time: {}".format(end - start))
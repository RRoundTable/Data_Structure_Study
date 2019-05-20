import time
import math
import numpy as np

# dynamic programing: runtime error
def solution(a):
    a = set(a)
    return len(a)

# test1
a = [2, 1, 1, 2, 3, 1]
expected = 3
print("1: {}".format(solution(a) == expected))


# test6
a = list(np.random.randint(-1000000, 1000000, 1000000))
expected = 0
start = time.time()
print("5: {}".format(solution(a) == expected))
end = time.time()
print("time: {}".format(end - start))
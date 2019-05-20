import time
import math
import numpy as np


# moving average
def solution(a):
    l = len(a)
    total_min = min(a)
    examples = [2, 3] # 2, 3개의 인자만 구하면 된다. 4부터는 2, 3의 집합의 평균이다
    result = []
    for e in examples:
        queue = []
        for i, x in enumerate(a):
            queue.append(x)
            if len(queue) == e:
                min_v = sum(queue) / e
                result.append((min_v,i - e + 1))
                if min_v == total_min:
                    return i - e + 1
                queue.pop(0)
    result = sorted(result, key=(lambda x: x[0]))
    return result[0][1]

# test1
a = [4, 2, 2, 5, 1, 5, 8]
expected = 1
print("1: {}".format(solution(a) == expected))

# test2
a = [4, 2, 4, 5, 5, 1, 5, 3]
expected = 0
print("1: {}".format(solution(a) == expected))


# test3
a = [1, 1, 1, 1, 1, 1]
expected = 0
print("1: {}".format(solution(a) == expected))

# test4
a = [1, 7, 5, 5]
expected = 0
print("1: {}".format(solution(a) == expected))

# test5
a = [1, 7, 1, 7, 7]
expected = 0
print("1: {}".format(solution(a) == expected))


# test6
a = list(np.random.randint(-10000, 10000, 100000))
expected = 0
start = time.time()
print("1: {}".format(solution(a) == expected))
end = time.time()
print("time: {}".format(end - start))
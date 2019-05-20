import time
import math
import numpy as np

def solution(a, b, k):

    b1 = b // k
    a1 = a // k
    if a % k == 0:
        a1 -= 1
    result = b1 - a1
    return result

# test1
a, b, k = [6, 11, 2]
expected = 3
print("1: {}".format(solution(a, b, k) == expected))

# test2
a, b, k = [6, 11, 11]
expected = 1
print("2: {}".format(solution(a, b, k) == expected))


# test3
a, b, k = [6, 9, 2]
expected = 2
print("3: {}".format(solution(a, b, k) == expected))

# test4
a, b, k = [6, 9, 11]
expected = 0
print("4: {}".format(solution(a, b, k) == expected))



# test6
a, b, k = list(np.random.randint(0, 2000000000, 3))
expected = 0
start = time.time()
print("5: {}".format(solution(a, b, k) == expected))
end = time.time()
print("time: {}".format(end - start))
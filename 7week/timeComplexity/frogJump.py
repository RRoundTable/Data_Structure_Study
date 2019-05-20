import time
import math
def solution(x, y, d):

    distance = y - x
    if distance <= 0:
        return 0
    return math.ceil(distance / d)

# test1
x, y, d = (10, 85, 30)
expected = 3
print("1: {}".format(solution(x, y, d) == expected))

# test2
x, y, d = (100, 85, 30)
expected = 0
print("2: {}".format(solution(x, y, d) == expected))

# test3
x, y, d = (0, 8500000, 30)
expected = 0
print("3: {}".format(solution(x, y, d) == expected))

# test3
x, y, d = (0, 0, 30)
expected = 0
print("3: {}".format(solution(x, y, d) == expected))
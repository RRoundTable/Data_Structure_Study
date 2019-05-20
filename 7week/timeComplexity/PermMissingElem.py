import time
import math

def solution(a):
    # a : 1 ~ N+1
    l = len(a)
    total = set(list(range(1, l+2))) # O(1): set / O(N): range
    answer = total - set(a)
    return list(answer)[0]

# test1
a = [2, 3, 1, 5]
expected = 4
print("1: {}".format(solution(a) == expected))

# test2
a = [2, 3, 1, 5, 6]
expected = 4
print("2: {}".format(solution(a) == expected))

# test3
a = [2, 3, 4, 5]
expected = 1
print("3: {}".format(solution(a) == expected))

# test4
a = list(range(1,100000))
expected = 1000
start = time.time()
print("4: {}".format(solution(a) == expected))
end = time.time()
print("4 time: {}".format(end - start))
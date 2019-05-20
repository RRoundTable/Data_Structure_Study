import time
import math

def solution(n, a):
    counter = [0] * n
    # for i in range(n):
    #     counter[i] = 0
    max_v = 0 # save maximum value
    for i, e in enumerate(a):
        if e <= n:
            counter[e-1] += 1
            if max_v < counter[e-1]:
                max_v = counter[e-1]
        else:
            counter = [max_v] * n
    return counter

# test1
n = 5
a = [3, 4, 4, 6, 1, 4, 4]
expected = [3, 2, 2, 4, 2]
print("1: {}".format(solution(n, a) == expected))

# test2
n = 5
a = [3, 4, 4, 6, 1, 4, 4, 6]
expected = [4, 4, 4, 4, 4]
print("2: {}".format(solution(n, a) == expected))

# test3
n = 5
a = [3, 4, 4, 6, 1, 4, 1]
expected = [4, 2, 2, 3, 2]
print("3: {}".format(solution(n, a) == expected))

# test4
n = 5
a = [3, 4, 4, 6, 1, 4, 6, 6, 6]
expected = [3, 3, 3, 3, 3]
print("4: {}".format(solution(n, a) == expected))


# test3
n = 5
a = list(range(1,100000))
expected = [3, 3, 3, 3, 3]
start = time.time()
print("4: {}".format(solution(n, a) == expected))
end = time.time()
print("time: {}".format(end - start))

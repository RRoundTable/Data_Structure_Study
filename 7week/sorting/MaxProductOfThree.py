import time
import math
import numpy as np

# handling negative case
def solution(a):

    a_sorted = sorted(a, reverse=True)

    positive = [ e for e in a_sorted if e >= 0] # O(N)
    negative = [ e for e in a_sorted if e < 0] # O(N)
    negative = sorted(negative) # O(NlogN)
    if len(positive) >= 1: # positive result
        if len(negative) < 2: # error
            result =  positive[0] * positive[1] * positive[2]
            return result
        if len(positive) == 1 or len(positive) == 2:
            result = positive[0] * negative[0] * negative[1]
            return result
        nproduct = negative[0] * negative[1] * positive[0]
        pproduct = positive[0] * positive[1] * positive[2]
        if pproduct >= nproduct:
            return pproduct
        else:
            return nproduct

    else: # negative result

        result = negative[-1] * negative[-2] * negative[-3]

        return result


# test1
a = [-3, 1, 2, -2, 5, 6]
expected = 60
print(solution(a))
print("1: {}".format(solution(a) == expected))

# test2
a = [-3, -1, -1, -2, 5, 6]
expected = 36
print("2: {}".format(solution(a) == expected))

# test3
a = [-3, -1, -1, -2, -1, 6]
expected = 36
print("3: {}".format(solution(a) == expected))

# test4
a = [-3, -1, -1, -2, -1, -1]
expected = -1
print("4: {}".format(solution(a) == expected))


# test6
a = list(np.random.randint(-1000000, 1000000, 1000000))
expected = 0
start = time.time()
print("5: {}".format(solution(a) == expected))
end = time.time()
print("time: {}".format(end - start))
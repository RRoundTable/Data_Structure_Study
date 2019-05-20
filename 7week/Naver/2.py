import time
import numpy as np


# maximum
def solution(a, b):
    a1 = a // 2
    if a1 == 0:
        a1 = []
    else:
        a1 = [ 2 for i in range(a1)]
    a2 = a % 2
    if a2 == 0 :
        a2 = []
    else:
        a2 = [1 for i in range(a2)]

    b1 = b // 2
    if b1 == 0:
        b1 = []
    else:
        b1 = [2 for i in range(b1)]

    b2 = b % 2
    if b2 == 0:
        b2 = []
    else:
        b2 = [1 for i in range(b2)]
    A = a1 + a2
    B = b1 + b2
    total = len(A) + len(B)
    reverse = False
    if len(A) < len(B):
        tmp = A
        A = B.copy()
        B = tmp
        reverse = True
    result = ""
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    if len(A) - 1 > len(B):
        print(b1)
        B = b2 + [1 for i in range(len(b1) * 2 )]
    print(A , B, total)
    for i in range(total):
        if not reverse:
            if i % 2 == 0:
                result += "a" * A.pop(0)
            else:
                result += "b" * B.pop(0)
        else:
            if i % 2 == 0:
                result += "b" * A.pop(0)
            else:
                result += "a" * B.pop(0)

    return result

#
# def solution(a, b):
#     a1, a2 = a // 2, a % 2
#     b1, b2 = b // 2, b % 2
#
#     a_need = a1 + a2 - 1
#     b_need = b1 + b2 - 1
#
#     reverse = False
#     if a < b:
#         reverse = True
#
#
#
#
#
#
#
#     return None

# test1: correctness
a, b = [5, 3]
expected = "aabaabab"
print(solution(a, b) == expected)  # 17

# test1: correctness
a, b = [1, 4]
expected = "aabaabab"
print(solution(a, b))
print(solution(a, b) == expected)  # 17

# test1: correctness
a, b = [5, 2]
expected = "aabaabab"
print(solution(a, b))
print(solution(a, b) == expected)  # 17

# test4
a = np.random.randint(-10000, 10000, 100000)
start = time.time()
print(solution(a))
end = time.time()
print("time: {}".format(end - start))
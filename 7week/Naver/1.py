import time
import numpy as np
# maximum
def solution(a):

    max_slice = []
    used = []
    a_curr = [0] + a[:-1]

    result = [a[i] - a_curr[i] for i in range(len(a))] #
    index = [] # 앞 부분 제거
    for i, e in enumerate(result):
        if e > 0:
            index.append(i)

    size = []
    used = []
    for i, e in enumerate(index[:-1]):
        if e in used:
            continue
        s = 1
        used.append(e)
        if index[i+1] - e == 1:
            while True:
                s += 1
                i += 1
                if index[i+1] - e == 1:
                    continue
                else:
                    size.append(s)
                    break
        else:
            size.append(s)

    size = [0] + size
    max_v = max(size)

    final = [ i for i in index if size[i] == max_v]

    return None


def solution(a):
    max_slice = []
    used = []
    a_curr = [0] + a[:-1]

    result = [a[i] - a_curr[i] for i in range(len(a))]  #
    index = []  # 앞 부분 제거
    for i, e in enumerate(result):
        if e > 0:
            index.append(i)



    if len(index) == 1: # 하나도 없다면
        return list(range(len(a)))

    index_curr = [0] + index[:-1]
    print(index)
    result = [index[i] - index_curr[i] for i in range(len(index))]
    print(result)
    most = []
    used = []
    for i, e in enumerate(index):
        if i in used:
            continue
        cnt = 1
        stack = []
        if index[i] - index_curr[i] == 1:
            tmp = i
            stack = []
            while  i < len(a):
                used.append(i)
                stack.append(index[i])
                i += 1
                if i == len(a):
                    break
                if index[i] - index_curr[i] == 1:
                    cnt += 1
            most.append(stack)
        else:
            stack.append(index[i])
            most.append(stack)
    return None

def solution(a):
    a_curr = [0] + a[:-1]

    result = [a[i] - a_curr[i] for i in range(len(a))]
    index = []
    for i, e in enumerate(result):
        if e > 0:
            index.append(i)

    if len(index) == 1: # 하나도 없다면
        return 0

    used = []
    result = []

    for i, e in enumerate(index[:-1]):
        if i in used:
            continue
        stack = []
        stack.append(e)
        used.append(i)
        while i < len(a):
            if index[i+1] - e == 1: # 연속
                stack.append(index[i+1])
                used.append(i+1)
                i += 1
            else:
                break
        result.append(stack)
    if len(index) - 1 not in used:
        result.append([index[-1]])
    size = [len(r) for r in result]
    max_idx = size.index(max(size))
    if result[0] == [0]:
        result.pop(0)
        return result[max_idx-1][0] -1
    return result[max_idx][0] -1

def solution(a):
    l = len(a)
    a_curr = [0] + a[:-1]
    sub = [a[i] - a_curr[i] for i in range(l)]
    sub[0] = 0 # set 0-th
    indexs = []
    used = []
    for i, s in enumerate(sub):
        if i in used:
            continue
        stack = []
        used.append(i)
        if s > 0:
            while i < len(sub) and sub[i] > 0:
                stack.append(i)
                i += 1
                used.append(i)
        if stack == []:
            continue
        indexs.append(stack)
    if len(indexs) == 0:
        return 0

    size = [len(i) for i in indexs]
    max_idx = size.index(max(size))

    return indexs[max_idx][0] - 1

# test1: correctness
a = [2, 2, 2, 2, 1, 2, -1, 2, 1, 3]
expected = 4
print(solution(a) == expected)

# test2: correctness
a = [30, 20, 10]
expected = 0
print(solution(a) == expected)  # 17


# test1: correctness
a = [2, 2, 2, 0, 1, 2, -1, 2, 1, 3]
expected = 3
print(solution(a) == expected)

# test4
a = list(np.random.randint(-10000, 10000, 100000))

start = time.time()
print(solution(a))
end = time.time()
print("time: {}".format(end - start))
import time
import numpy as np

# time complexity: O(N * )
def solution(a, b):
    cnt = 0
    down = []
    up = []
    for i in range(len(a)):
        if b[i] == 1:
            down.append(i)
        else:
            if len(down) == 0:
                up.append(i)
            else:
                while True:
                    if len(down) == 0:
                        up.append(i)
                        break
                    tmp = down.pop(-1)
                    if a[tmp] > a[i]:
                        down.append(tmp)
                        break
                    else:
                        continue
    return len(up) + len(down)

# test1: correctness
a, b = [4, 3, 2, 1, 5], [0, 1, 0, 0, 0]
print(solution(a,b))

# test2: correctness
a, b = [4, 3, 2, 1, 5], [0, 1, 1, 0, 0]
print(solution(a,b))

# test3: correctness
a, b = [4, 3, 2, 6, 5], [0, 1, 1, 0, 0]
print(solution(a,b))

# test4: efficiency
a, b = list(range(100000)), list(np.zeros(100000))
start = time.time()
print(solution(a,b))
end = time.time()
print(end - start)

# test5: efficiency
a, b = list(range(100000)), list(np.random.randint(0,1,100000))
start = time.time()
print(solution(a,b))
end = time.time()
print(end - start)
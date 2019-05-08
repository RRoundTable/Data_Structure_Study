
import time

def solution(a):
    a.append(0)
    a = set(a)
    a = sorted(a)  # sorting
    if a.index(0) == len(a) - 1:
        return 1
    a = a[a.index(0) + 1:]
    for i, e in enumerate(a):
        if i + 1 == e:
            continue
        else:
            return i + 1
    return e + 1

# test1
a = [1, 3, 6, 4, 1, 2]
print(solution(a)) # 5

# test2
a = [-1, -3]
print(solution(a)) # 1

# test3
a = [1, 2, 3]
print(solution(a)) # 4

# test4
a = [-1, 2, 0, 1000]
print(solution(a)) # 1

# test5
a = [-1000, 20, 1, 1000]
print(solution(a)) # 2

# test6
a = [-1000, 20, 1, 2, 3, 4, 1000]
print(solution(a)) # 5


# test8 : performance

a = list(range(100000))
a.pop(7000)

print(solution(a))

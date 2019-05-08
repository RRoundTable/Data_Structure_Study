import numpy as np

def solution(a):
    total_sum = sum(a)
    goal = total_sum / 2.0
    cumsum = [None] * (len(a)-1)
    tmp = 0
    for i, e in enumerate(a[:-1]):
        tmp += e
        cumsum[i] = int(abs(tmp - (total_sum - tmp)))
        if int(abs(tmp - (total_sum - tmp))) == 0:
            return 0

    return min(cumsum)

# goal 설정하기 다시

a = [3, 1, 2, 4, 3]
print(solution(a))

# element중 -가 있는 경우
a = [-1, -2, 4, 5, 6, 7, 8]
print(solution(a))


# element의 수가 2
a = [-1000, 2000]
print(solution(a))
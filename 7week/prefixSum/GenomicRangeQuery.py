
# prefix sum: 구간 합
# 범위 설정 자세히 확인하기

# s : non-empty 100,000, only upper-case English
# p : non-empty 50,000, integer
# q : non-empty 50,000, integer
# P[K] ≤ Q[K], where 0 ≤ K < M
# efficient algorithm : 효율성

import time
from multiprocessing import Pool

dna2fac = {"A": 1, "C": 2, "G":3, "T": 4}
# time complexity : average case
def solution(s, p, q):
    answer = []
    for i in range(len(p)):
        if p[i] == q[i]:
            result = dna2fac[s[p[i]]]
        else:
            if 'A' in s[p[i]:q[i]+1]:
                result = 1
            elif 'C' in s[p[i]:q[i]+1]:
                result = 2
            elif 'G' in s[p[i]:q[i]+1]:
                result = 3
            else:
                result = 4
        answer.append(result)
    return answer


# test1
s, p, q = 'CAGCCTA', [2, 5, 0], [4, 5, 6]
print(solution(s, p, q)) # [2, 4, 1]

# test2
s, p, q = "CCCCCCCCCC", [2, 5, 0], [4, 5, 6]
print(solution(s, p, q)) # [2, 2, 2]

# test3
start = time.time()
s, p, q = "CCCCCCCCCC" * 1000, list(range(1000)), list(range(1,1001))
print(solution(s, p, q)) # [2, 2, 2]
end = time.time()
print(end - start)

# test4
s, p, q = "AAAAAAAAAAAAAAA" * 100000, list(range(500000)), list(range(100,500100))
start = time.time()
print(solution(s, p, q)) # [2, 2, 2]
end = time.time() # 3초안에
print(end - start)

# test5
s, p, q = "AAAAAAAAAAAAAAA" * 100000, [0] * 500000, [100000] *  500000
start = time.time()
print(solution(s, p, q)) # [2, 2, 2]
end = time.time() # 3초안에
print(end - start)



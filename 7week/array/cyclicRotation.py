
# performance는 고려하지 않아도 된다
from collections import OrderedDict
def solution(a, k):
    if len(a) == 0:
        return []
    # k가 클 경우
    idx2ele = {} # index
    end_idx = len(a) - 1
    try:
        k = k % len(a)
    except:
        print("k is 0")
    for i, e in enumerate(a):
        if i + k > end_idx:
            idx =  i + k - end_idx - 1
            idx2ele[idx] = e
        else:
            idx = i + k
            idx2ele[idx] = e
    idx2ele = OrderedDict(sorted(idx2ele.items(), key=(lambda x:x[0])))
    answer = [item[1] for item in idx2ele.items()]
    return answer


# Test case
a1 = [3, 8, 9, 7, 6]
k1 = 10

a2 = [0, 0, 0] # test case를 아주 꼼꼼히 확인하기 : 왜 0을 줬을까?
k2 = 1

a3= [3, 8, 8, 7, 6]
k3 = 3

a4 = [-1, -2, 3, 4, 5]
k4 = 6

a5 = []
k5 = 0
print(solution(a1, k1))
print(solution(a2, k2))
print(solution(a3, k3))
print(solution(a4, k4))
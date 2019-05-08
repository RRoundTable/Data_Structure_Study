from itertools import combinations


# disk 할당 : 무엇을 없애야 동등하게 일을 하는가, 두 개 없애기

def solution(A):
    N = len(A)
    for i in range(N-1):
        first = sum(A[:i])
        
        if first < (sum(A[i+1:]) - max(A[i+1:]))/2:
            continue
        if first >  (sum(A[i+1:]) - min(A[i+1:]))/2:
            continue
        for j in range(i, N):
            second = sum(A[i+1 :j])
            if second > first:
                break
            if second != first:
                continue
            third = sum(A[j+1:])
            if first == second and second == third:
                return True
    return False

def solution(a):
    total_sum = sum(a)
    residual = total_sum % 3 # residual
    a_i = [(e,i) for i, e in enumerate(a)]
    # 두 element를 뽑는 조합
    comb = list(combinations(a_i, 2))
    comb = [c for c in comb if (c[0][0] + c[1][0]) % 3 == residual]
    if len(comb) == 0:
        return False
    for fir, sec in comb:
        goal = (total_sum - (fir[0] + sec[0])) / 3
        if sum(a[: fir[1]]) == goal:
            if sum(a[fir[1]+1:sec[1]]):
                if sum(a[sec[1]+1:]) == goal:
                    return True
                    break
            else:
                continue
        else:
            continue
    return False
A = [1, 3, 4, 2, 2, 2, 1, 1, 2]
B = [1, 1, 1, 1, 1, 1]
print(solution(B))
print(len(A))
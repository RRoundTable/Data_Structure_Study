

# 주사위 문제
def solution(A):
    A = sorted(A)
    count  = 0
    for i in range(len(A) - 1):
        if A[i] == A[i+1]:
            continue
        elif A[i] + A[i+1] ==7:
            count += 2
        else:
            count +=1

    return count


A = [1, 2, 3]



import math

# 최대 root수
def solution(A, B):
    count = []
    for i in range(A, B + 1):
        count.append(check(i))
    return max(count)

def check(num):
    cnt = 0
    while True:
        if math.sqrt(num) == int(math.sqrt(num)):
            cnt += 1
            num = math.sqrt(num)
            continue
        else:
            break
    return cnt

def solution(a, b): # 경계를 가지고 파악하는 것이 좋다
    count = 0
    while a >= 1 and b >= 2:
        a = math.sqrt(a)
        b = math.sqrt(b)
        count += 1
    return count



A = 10
B = 20


print(solution(A,B))
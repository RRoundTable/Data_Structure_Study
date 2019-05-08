

def solution(N):
    i = 0
    binary = bin(N)[2:]

    count = []
    for i, b in enumerate(binary):
        if b == "1":
            count.append(i)
        if i == len(binary) - 1:
            count.append(i+1)
    if len(count) == 2:
        return 0
    result = [count[i+1] - count[i] - 1 for i in range(len(count)-1)]
    result.pop(-1) # 6의 경우  110
    return max(result)

N = 1041
result = 5
print(type(bin(1041)))
print(solution(N))


print(bin(100000000)) # error
print(bin(6))
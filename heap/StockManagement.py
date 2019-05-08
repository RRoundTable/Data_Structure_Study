
from heapq import heappop, heapify, heappush


def solution(stock, dates, supplies, k):
    for i in dates[::-1]: # 거꾸로
        if i > k:
            dates.pop()
            supplies.pop()
        else:
            break

    dates.append(k) # 마지막 dates 추가
    dates.pop(0) # 첫 번째 공급일 지우기
    sum_  = stock
    count = 0
    heap = [-supplies[0]]
    heapify(heap)

    for index,day in enumerate(dates):
        while sum_ < dates[index]: # 공급을 받아야 되는 상황
            lar = heappop(heap)
            sum_ += -lar
            count += 1
        if dates[index] != k:
            heappush(heap, -supplies[index + 1])
    return count

def solution_(stock, dates, supplies, k):
    answer, start = 0, 0
    plan = []
    n = len(dates)
    while stock < k:
        for i in range(start, n):
            if dates[i] <= stock:
                heappush(plan, -supplies[i])
            else:
                start = i
                break
        answer += 1 
        stock += - heappop(plan) # 공급받기
    return answer

stock = 4
dates = [4, 10, 15]
supplies = [20, 5, 10]
k = 30


print(solution(stock, dates, supplies, k))
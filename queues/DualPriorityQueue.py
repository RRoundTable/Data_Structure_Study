
from heapq import heappop, heappush, heapify
from collections import deque

def solution(operations):
    answer = []
    oper = [o.split(" ") for o in operations]
    queue = []

    while len(oper) != 0:
        tmp_oper = oper.pop(0)
        if tmp_oper[0] == "I":
            queue.append(int(tmp_oper[1]))
        elif tmp_oper[0] == "D":
            if len(queue) == 0:
                continue
            if tmp_oper[1] == "1":
                queue.pop(-1)
            else:
                queue.pop(0)
        queue = sorted(queue)

    if len(queue) == 0:
        answer =[0, 0]
    else:
        answer = [max(queue), min(queue)]
    return answer


oper1 = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
result1 = [0, 0]
oper2 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
retulst = [333, -45]


print(solution(oper2))
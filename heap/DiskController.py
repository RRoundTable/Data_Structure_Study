from heapq import heapify, heappop, heappush
import numpy as np

def solution(jobs):
    heap = [] # ele : [arrive_time, term]
    result = [] # Ordered [arrive_time, end_time]
    indexs = []
    task_arr = []
    task_len = []
    jobs = sorted(jobs, key=(lambda x: x[0])) # start 순서대로 정렬하기
    for i, item in enumerate(jobs):
        task_arr.append(item[0])
        task_len.append(item[1])

    for idx, l in enumerate(task_len):
        print("indexs : {}".format(indexs))
        if idx in indexs:
            continue
        i = idx
        while task_arr[idx] == task_arr[i]:
            heap.append([task_arr[i], task_len[i]])
            indexs.append(i)
            i += 1
            if i == len(task_arr):
                break

        print("idx : {}".format(idx))
        start = task_arr[idx]
        heap = sorted(heap, key=(lambda x: x[1]))
        while heap != []:
            arr, term = heap.pop(0)
            result.append([arr, start + term])
            start += term
            if i >= len(task_arr):
                continue
            while start >= task_arr[i]:
                if i + 1 not in indexs:
                    heap.append([task_arr[i], task_len[i]])
                    indexs.append(i)
                i += 1
                if i  == len(task_arr):
                    break
            heap = sorted(heap, key=(lambda x: x[1]))
    print(result)
    result = [x[1] - x[0] for x in result]
    print(result)
    return int(sum(result)/len(result))

jobs = [[0, 3], [1, 9], [2, 6]]
answer1 = 9

jobs = [[0, 4], [0, 3], [1, 9], [2, 6]]        # 3, 4, 6, 9 // 3, 7, 13, 22
answer2 = 10
j = [ i for i in range(len(jobs))]

print(solution(jobs))

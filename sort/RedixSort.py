import random
import time
import numpy as np

N=100
lstNumbers=list(range(N))
random.seed(1)
random.shuffle(lstNumbers)

print(lstNumbers)

def get_digit(num, index):
    """
    :param num: 10진법 숫자
    :param index
    :return: index번째 digit
    """
    return int(num / (10 ** index)) % int(10)


def reditSort(lstNum):
    """
    :param lstNum: unsorted integer list
    :return: sorted list
    """
    max_val = -9999

    for iter in range(len(lstNum)):
        if lstNum[iter] > max_val:
            max_val = lstNum[iter]

    D = int(np.log10(max_val)) # 최댓값의 자릿수 : digit bucket의 수
    for iter in range(0, D+1):
        bucket = []
        for i in range(0, 10):
            bucket.append([int(ele) for ele in lstNum if get_digit(ele, iter) == i])
        lstNum =[]
        for b in bucket:
            for ele in b:
                lstNum.append(ele)

    return lstNum

print(reditSort(lstNumbers))




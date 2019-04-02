import random
import time

N=100
lstNumbers=list(range(N))
random.seed(1)
random.shuffle(lstNumbers)

print(lstNumbers)

def quickSort(lstNum, pivot = 0):

    if len(lstNum) <= 1 :
        return lstNum
    pivot_value = []
    less = []
    greater = []
    for iter in range(len(lstNum)):
        if pivot == iter :
            pivot_value.append(lstNum[iter])
        elif lstNum[iter] > lstNum[pivot]:
            greater.append(lstNum[iter])
        elif lstNum[iter] < lstNum[pivot]:
            less.append(lstNum[iter])

    return quickSort(less) + pivot_value + quickSort(greater)

print(quickSort(lstNumbers))
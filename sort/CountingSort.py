import random
import time

N=100
lstNumbers=list(range(N))
random.seed(1)
random.shuffle(lstNumbers)

print(lstNumbers)


def countSort(lstNum):
    """
    :param lstNum:  unsorted integer list
    :return: sorted lstNum
    """
    min_val = min(lstNum)
    max_val = max(lstNum)

    lst_len = len(list(range(min_val, max_val)))
    result =[]
    count=[0]*lst_len # count의 index는 lstNum의 element

    for i in range(len(lstNum)):
        count[lstNum[i] + min_val - 1] += 1

    idx = 0
    for ele in count:
        if ele != 0:
            result += [idx - min_val] * ele
        idx += 1

    return result


print(countSort(lstNumbers))

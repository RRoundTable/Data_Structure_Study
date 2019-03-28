import random
import time
import math
N=8
lstNumbers=list(range(N))
random.seed(1)
random.shuffle(lstNumbers)

""" 홀수인 경우 어떻게 대처할지"""

def mergeSort(lstNumbers, two_element=None):
    """
    decomposition phase

    Turning point

    Aggregation phase
    """
    total_len=len(lstNumbers)
    two_element=decomposition(lstNumbers)

    while True:
        two_element=aggregation(two_element)
        if len(two_element)==1:
            break
    return two_element

def decomposition(lstNumbers, two_element=None):
    break_point = int(len(lstNumbers) / 2)
    a = lstNumbers[:break_point]
    b = lstNumbers[break_point:]
    if two_element == None:
        two_element = []
    for i in [a, b]:
        if len(i) == 2:
            if i[0] > i[1]:
                tmp = i[0]
                i[0] = i[1]
                i[1] = tmp
            two_element.append(i)
        elif len(i) == 1:
            two_element.append(i)
        else:
            two_element = decomposition(i, two_element)
    return two_element

def aggregation(two_element, result=None):

    iter_num=int(len(two_element)/2)
    if iter_num==0:
        return two_element
    if result==None:
        total_result=[]
    for iter in range(iter_num):
        i = 0
        j = 0
        result=[]
        a_len = len(two_element[iter * 2])
        b_len = len(two_element[iter * 2 + 1])
        while True:
            if two_element[iter*2][0]< two_element[iter*2+1][0]:
                result.append(two_element[iter*2][0])
                two_element[iter*2]=two_element[iter*2][1:]
                i+=1
            elif two_element[iter*2][0]> two_element[iter*2+1][0]:
                result.append(two_element[iter* 2+1][0])
                two_element[iter * 2+1] = two_element[iter * 2+1][1:]
                j += 1
            else :
                result.append(two_element[iter * 2][0])
                two_element[iter * 2 ] = two_element[iter * 2 ][1:]
                i += 1
            if i==a_len:
                result+=two_element[iter*2+1]
                total_result.append(result)
                break
            elif j==b_len:
                result+=two_element[iter*2]
                total_result.append(result)
                break

    return total_result


print(lstNumbers)
print(mergeSort(lstNumbers))
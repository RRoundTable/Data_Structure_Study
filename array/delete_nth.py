
# 문제
"""
Given a list lst and a number N, create a new list
that contains each number of the list at most N times without reordering.
For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
which leads to [1,2,3,1,2,3]

"""


exList= [1,2,3,1,2,1,2,3]

# 내가 해결한 방법
def delete(array,n):

    unique=[]
    for i in array:
        if i in unique:
            continue
        unique.append(i)

    count=[0]*len(unique) # 각 인덱스가 count값을 가지고 있는다

    result=[]

    for i in array:
        if count[unique.index(i)]<n:
            print(unique.index(i))
            result.append(i)
            count[unique.index(i)]+=1
    return result


print(delete(exList,2))


# 모범답안
"""
collection을 사용하였다
"""
import collections

def delete_ex(array,n):
    result=[]
    counts=collections.defaultdict(int)

    for i in array:
        print("array : "+str(i))
        print(counts[i])
        if counts[i]<n: # count[i] : i성분의 노출빈도를 나타낸다
            result.append(i)
            counts[i]+=1

    return result

def delete_nth(array, n):
    result = []
    counts = collections.defaultdict(int)  # keep track of occurrences

    for i in array:

        if counts[i] < n:
            result.append(i)
            counts[i] += 1

    return result

print(delete_nth(exList,2))

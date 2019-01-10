"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.
For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""


def josephus(array):
    """
    array의 길이는 3의 배수라고 가정한다
    :param array: circular array
    :return: order나가는 순서
    """
    tmp=array
    order=[]
    input_len=len(array)

    Done=True
    counter=0
    while Done:
        tmp=array
        if len(order)==input_len:
            Done=False

        for ele in array:
            if  (counter+1)%3==0 and len(array)>2:
                print(counter+1, "번째")
                print("빠져나가는 ele : ",ele)
                order.append(ele)
                del tmp[tmp.index(ele)]

                counter=0
                array=tmp[2:]+tmp[:2]
                print("array : ", array)
                print("len array: ",len(array))
                break
            elif len(array)==2:
                order+=array
                array=[]
            else:
                counter+=1






    return order

test=[1,2,3,4,5,6,7,8,9]

print(josephus(test))
"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections import Iterable
nested_list = [2, 1, [3, [4, 5], 6], 7, [8]]

# recursive한 problem
def flatten(input_arr, output_arr=None):
    if output_arr==None:
        output_arr=[]

    for ele in input_arr:
        print("ele: ", ele)
        if type(ele)!=list:
            print(type(ele))
            print("append!!")
            output_arr.append(ele)
            print("output_Arr : ",output_arr) # 연결이 안된다
        else:
            output_arr+=flatten(ele) # recursive connectivity

    return output_arr


print(flatten(nested_list))

# return iterator
def flatten_iter(iterable):
    for ele in iterable:
        if isinstance(ele,iterable): # class의 인스턴스인지 파악한다
            yield  from flatten(ele)
        else :
            yield  ele
"""
Sometimes you need to limit array result to use. Such as you only need the
 value over 10 or, you need value under than 100. By use this algorithms, you
 can limit your array to specific value
If array, Min, Max value was given, it returns array that contains values of
 given array which was larger than Min, and lower than Max. You need to give
 'unlimit' to use only Min or Max.
ex) limit([1,2,3,4,5], None, 3) = [1,2,3]
Complexity = O(n)
"""


def limit(array, min_v, max_v):
    """

    :param array: 해당 array
    :param min: 최소값
    :param max: 최대값
    :return: 최소값~최대값 사이의 array

    None에 대해서 어떻게 접근할 것인가
    """
    if min_v == None:
        min_v = min(array)
    if max_v ==None:
        max_v=max(array)
    result=[]
    for ele in array:

        if ele >=min_v and ele<=max_v:
            result.append(ele)
    return result


print(limit([1,2,3,4,5], None, 3))
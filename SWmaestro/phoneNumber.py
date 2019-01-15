"""
전화번호 문제

전화번호가 아래와 같이 출력되는데

010-1234-1234
010-1234-1234
010-2222-2222
010-2222-2222
010-3333-3333
010-2222-2222

이것을 앞으로는
010-1234-1234(2)
010-2222-2222(2)
010-3333-3333
010-2222-2222

로 중복되는 것을 합쳐서 내보내게 업데이트하려고 한다. 구현하라

"""

def phoneNumber(array,count=0):

    """

    :param array: 전화번호 순서대로
    :return: 전화번호 중복처리된 것
    """

    result=[]


    for i in range(len(array)):
        if i<len(array)-1 and array[i] == array[i + 1]:
            count += 1
            continue

        else :
            result.append([array[i],count+1])
            count=0

    return result

array=['010-1234-1234',
'010-1234-1234',
'010-2222-2222',
'010-2222-2222',
'010-3333-3333',
'010-2222-2222',
'010-2222-2222',
'010-2222-2222']

print(phoneNumber(array))
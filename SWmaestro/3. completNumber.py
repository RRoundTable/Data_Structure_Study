"""
완전수 구하는 문제

완전수란, 자기자신을 제외한 모든 약수를 더 했을 때 자기자신이 되는 수


예시)

6의 약수 1,2,3,6

6=1+2+3

6은 완전수
"""


def completeNumber(n):

    """
    이중 for문으로 구하여라
    :param N:
    :return: N이하의 모든 자연수 집합
    """
    completeNum=[] # 완전수 집합

    for i in range(1,n+1):
         # i는 숫자

        divisor=[]  # 약수
        for j in range(1,int(i/2)+1): # 해당 숫자의 반 정도까지만
            if i%(j)==0: # j는 i의 약수

                divisor.append(j) # 약수 추가

        if i==sum(divisor): # 완전수가 맞다면
            completeNum.append(i)

    return completeNum


print(completeNumber(10000))
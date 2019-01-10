"""
치킨회사 A,B

A는 무조건 3조각씩
B는 무조건 7조각씩 판다

길동이가 정확히 N조각의 치킨을 먹고 싶다고 입력하면, 정확히 N조각을 먹을 수 있는지 없는지 판별하여라
"""



def chicken(n):
    """

    :param n: 먹고 싶은 조각의 수
    :return: True or False

    N=3*a1+나머지1
    N=7*a2+나머지2
    2N=3*a1+나머지1+7*a2+나머지2
    나머지1+나머지2가 7로 나누어 떨어진다면? True


    """

    if n%3+n%7==7:
        result=True
    else:
        result=False

    return result


print(chicken(25))

"""
첫 번째 상태와 마지막 상태를 주고
There is a parking lot with only one empty spot. Given the initial state
of the parking lot and the final state.
자동차를 원래 있떤 자리에서 옮기고 빈 자리로 옮겨라
move a car out of its place and move it into the empty spot.

# 재배치하는데 최소한의 거리를 구하여라
The goal is to find out the least movement needed to rearrange
the parking lot from the initial state to the final state.
Say the initial state is an array:
[1, 2, 3, 0, 4],
where 1, 2, 3, 4 are different cars, and 0 is the empty spot.
And the final state is
[0, 3, 2, 1, 4].
We can swap 1 with 0 in the initial array to get [0, 2, 3, 1, 4] and so on.
Each step swap with 0 only. 0하고만 자리를 바꿀 수 있다.
Edit:
Now also prints the sequence of changes in states.
Output of this example :-
initial: [1, 2, 3, 0, 4]
final:   [0, 3, 2, 1, 4]
Steps =  4
Sequence :
0 2 3 1 4
2 0 3 1 4
2 3 0 1 4
0 3 2 1 4
"""

initial_s=[1, 2, 3, 0, 4]
final_s= [0, 3, 2, 1, 4]

def parking(initial_s,final_s):

    """
    일치하는 차량은 유지한다.
    한번에 바꿔서 가능한 차량 : 0과 바로 바꾸면 되는 차량
    0 위치는 맞으나 다른 차량의 위치는 맞지 않는 경우
        0을 움직여 다른 하나를 맞춘다
    :param initial_s:
    :param final_s:

    print("current state : ", current_state)
    steps
    :return:

    """
    Done=True
    step = 0
    while Done:

        right_place, wrong_place, zero_index = check_place(initial_s,final_s)
        for wrong_ele in wrong_place:
            wrong_index=initial_s.index(wrong_ele)
            print("check1")
            print(zero_index)
            print(wrong_index)
            if zero_index==final_s.index(wrong_ele): # zero와 wrong 교환
                print("check2")
                initial_s[zero_index]=wrong_ele
                initial_s[wrong_index]=0
                step+=1


        print('check')
        print(check_place(initial_s, final_s))
        right_place, wrong_place, zero_index = check_place(initial_s, final_s)
        if len(wrong_place)!=0: # 흔들기
            wrong_index = initial_s.index(wrong_place[0])
            print("wrong index , : ",wrong_index)
            initial_s[zero_index] = wrong_place[0]


            initial_s[wrong_index]=0
            print("zero 위치")
            print(initial_s)
            step+=1


        if len(wrong_place)==0: # 끝
            Done=False


    return initial_s, step


# 바꿔야할 대상 확인하기
def check_place(initial_s,final_s):
    assert len(initial_s)==len(final_s)
    right=[]
    wrong=[]
    zero=None
    for i in range(len(initial_s)):
        if initial_s[i]==final_s[i] and initial_s[i]!=0:
            right.append(initial_s[i])
        elif initial_s[i]!=final_s[i] and initial_s[i]!=0:
            wrong.append(initial_s[i])
        else:
            zero=i
    return right, wrong, zero


print(check_place(initial_s,final_s)) # 맞음

print(parking(initial_s,final_s))
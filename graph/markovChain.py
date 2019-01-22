import random

'''
   A    E
A 0.6  0.4
E 0.7  0.4
'''
my_chain = {
    'A': {'A': 0.6,
          'E': 0.4},
    'E': {'A': 0.7,
          'E': 0.3}
}

def __choose_state(state_map):

    choice=random.random()
    probability_reached=0
    for state, prob in state_map.items():
        print("state : {}".format(state))
        print("prob : {}".format(prob))
        probability_reached+=prob
        if probability_reached>choice: # 한번에 안넘어가면 바로 다음 state로 변환
            return state


def next_state(chain, current_state):

    next_state_map=chain.get(current_state) # next state로 가는 mapping
    next_state=__choose_state(next_state_map)
    print("next_stae_map  : {}".format(next_state_map))
    print("next_stae  : {}".format(next_state))
    return next_state


# generator
def iterating_markov_chain(chain, state):

    while True:
        state=next_state(chain,state)

        yield state



for i in iterating_markov_chain(my_chain,"A"):
    print(i)

#next_state(my_chain,"E")
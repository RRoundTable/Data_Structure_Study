"""
# stack 구현하기


- stack

last-in-first-out
나중에 들어온 것이 먼저 나가는 구조
"""

# 한쪽 방향으로 된 linked list
class linkedList:
    def __init__(self, value):
        # self.node=None
        self.value=value
        self.nextNode=None

    def getValue(self):

        return self.value

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self,nextNode):
        self.nextNode=nextNode


# a=linkedList(10)
# b=linkedList(20)
#
# a.setNextNode(b)
#
# print(a.getNextNode().getValue())

class stack:
    def __init__(self):
        self.node=""

    def insert(self):

    def delete(self):

    def 



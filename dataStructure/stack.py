


"""
# stack 구현하기


- stack

last-in-first-out
나중에 들어온 것이 먼저 나가는 구조
"""


class Node:
    nodeNext=""
    value=""
    blnHead=False
    blnTail=False

    def __init__(self, objValue='',nodeNext="",blnHead=False,blnTail=False):
        self.nodeNext=nodeNext
        self.value=objValue
        self.blnHead=blnHead
        self.blnTail=blnTail

    def getValue(self):

        return self.value

    def setValue(self,value):

        self.value=value

    def getNext(self):
        return self.nodeNext

    def setNext(self,nodeNext):
        self.nodeNext=nodeNext

    def isHead(self):
        return self.blnHead

    def isTail(self):
        return self.blnTail


class SinglyLinkedList:
    nodeHead=""
    nodeTail=""
    size=0

    def __init__(self):
        self.nodeTail=Node(blnTail=True)
        self.nodeHead=Node(blnHead=True,nodeNext=self.nodeTail) # 시작과 끝


    def insertAt(self,objInsert, idxInsert):
        nodeNew=Node(objValue=objInsert)
        nodePrev=self.get(idxInsert-1)
        nodeNext=nodePrev.getNext()
        nodePrev.setNext(nodeNew)
        nodeNew.setNext(nodeNext)
        self.size=self.size+1

    def removeAt(self, idxRemove):
        nodeRemove=self.get(idxRemove)

        nodePrev=self.get(idxRemove-1)
        nodeNext=nodeRemove.getNext()

        nodePrev.setNext(nodeNext)
        self.size=self.size-1
        return nodeRemove.getValue()


    # idxRetrieve번째의 노드를 구한다
    def get(self, idxRetrieve):
        nodeReturn=self.nodeHead
        for itr in range(idxRetrieve+1):
            nodeReturn=nodeReturn.getNext()
        return nodeReturn


    def printStatus(self):
        nodeCurrent=self.nodeHead
        while nodeCurrent.getNext().isTail()==False:
            nodeCurrent=nodeCurrent.getNext()
            print(nodeCurrent.getValue())
        print("\n")


    def getSize(self):
        return self.size

class stack:
    def __init__(self):
        self.instance=SinglyLinkedList()

    def insert(self, value):
        return self.instance.insertAt(value, 0)

    def delete(self):
        return self.instance.removeAt((0))


stack=stack()
stack.insert("a")
stack.insert("b")
stack.insert("c")


print(stack.delete()) # c
print(stack.delete()) # b
print(stack.delete()) # a



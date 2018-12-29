
# treeNode의 variable과 method를 선언
class TreeNode:
    nodeLHS=""
    nodeRHS=""
    nodeParent=""
    value=""

    def __init__(self, value, nodeParent):
        self.value=value
        self.nodeParent=nodeParent

    # 왼쪽(작은값) 받기
    def getLHS(self):
        return self.nodeLHS

    # 오른쪽(큰값) 받기
    def getRHS(self):
        return self.nodeRHS

    # root값 받기
    def getValue(self):
        return self.value
    # parent값 받기
    def getParent(self):
        return self.nodeParent
    # setting LHS
    def setLHS(self,LHS):
        self.nodeLHS=LHS

    # setting RHS
    def setRHS(self,RHS):
        self.nodeRHS=RHS

    # setting Node
    def setValue(self, value):
        self.value=value

    # setting parent
    def setParent(self, nodeParent):
        self.nodeParent=nodeParent
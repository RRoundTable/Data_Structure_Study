from TreeNode import *

class BinarySearchTree:
    root=""

    def __init__(self):
        pass

    def insert(self,value,node=""):

        if node=="": # value를 연결할 노드가 없다면
            node=self.root # root를 노드라고 생각한다
        if self.root=="": # root가 지정되어 있지 않다면
            self.root=TreeNode(value,"") # root를 지정한다
            return

        # 삽입할려는 value가 기존 노드의 value와 같다면 끝
        if value==node.getValue():
            return

        #  삽입할려는 value가 기존 노드의 value보다 크다면
        if value> node.getValue():
            if node.getRHS()=="": # 오른쪽이 비어 있다면
                node.setRHS((TreeNode(value,node)))
            else: # 기존에 오른쪽에 지정된 것이 있다면
                self.insert(value,node.getRHS()) # recursion : node.getRHS가 중심이 된다.

        #  삽입할려는 value가 기존 노드의 value보다 작다면
        if value < node.getValue():
            if node.getLHS() == "": # 지정된 것이 없다면
                node.setLHS((TreeNode(value, node)))
            else: # 지정된 것이 있다면
                self.insert(value, node.getLHS())


    # search 함수

    def search(self,value,node=""):

        if node=="": # node를 지정하지 않았다면
            node=self.root # root가 기준 node가 된다

        if value==node.getValue():
            return True
        # 찾으려는 value가 node가 가진 값보다 크다면
        if value>node.getValue():
            if node.getRHS()=="": # 오른쪽의 값이 없다면
                return False # 실패
            else:
                return self.search(value, node.getRHS()) # 있다면, recursion

        if value<node.getValue():
            if node.getRHS()=="":
                return False
            else:
                return self.search(value, node.getLHS())



    def delete(self,value,node=""):

        if node=="":
            node=self.root
        if node.getValue() < value:
            return self.delete(value,node.getRHS())
        if node.getValue() > value:
            return self.delete(value, node.getLHS())
        if node.getValue() == value:
            if node.getLHS() !="" and node.getRHS()!="": # 해당 노드가 RHS,LHS 모두 가지고 있다면
                nodeMin=self.findMin(node.getRHS())
                node.setValue(nodeMin.getValue())
                self.delete(nodeMin.getValue(), node.getRHS())
                return
            parent=node.getParent()
            if node.getLHS()!="": # 해당노드가 LHS만 가지고 있다면
                if node==self.root:
                    self.root=node.getLHS()
                elif parent.getLHS()==node:
                    parent.setLHS(node.getLHS())
                    node.getLHS().setParent(parent)

                else :
                    parent.setRHS(node.getLHS())
                    node.getLHS().setParent(parent)
                return

            if node.getRHS()!="": # 해당노드가 RHS만 가지고 있다면

                if node == self.root:
                    self.root = node.getRHS()
                elif parent.getRHS() == node: # 제거할 노드가 parent의 RHS라면
                    parent.setRHS(node.getRHS()) # 제거할 노드의 RHS를 연결한다
                    node.getRHS().setParent(parent)

                else: # 제거할 노드가 parent의 LHS라면
                    parent.setLHS(node.getLHS())
                    node.getLHS().setParent(parent)
                return
            if node==self.root:
                self.root=""
            elif parent.getLHS()==node:
                parent.setLHS('')
            else:
                parent.setRHS('')
            return

    def findMax(self,node=""):
        if node=="":
            node=self.root
        if node.getRHS()=='':
            return node
        return self.findMax(node.getRHS())

    def findMin(self, node=""):
        if node=="":
            node=self.root
        if node.getLSH()=="":
            return node
        return self.findMin(node.getLHS())

    def traverseInOrder(self, node=""):
        # 작은 것부터 큰거 순으로 나열한다
        if node=="":
            node=self.root
        ret=[] # 나열하는 값
        if node.getLHS() !="": # LHS가 존재한다면
            ret=ret+self.traverseInOrder(node.getLHS())
        ret.apppend(node.getValue())
        if node.getRHS()!="":
            ret=ret+self.traverseInOrder(node.getRHS())
        #ret.append(node.getValue())
        return ret

    def traversePreOrder(self, node=""):
        # 위에서 부터 LHS -> RHS
        if node=="":
            node=self.root
        ret=[]
        ret.apppend(node.getValue())
        if node.getLHS() !="": # LHS가 존재한다면
            ret=ret+self.traverseInOrder(node.getLHS())
        if node.getRHS()!="":
            ret=ret+self.traverseInOrder(node.getRHS())

        return ret

    def traversePostOrder(self, node=""):
        if node=="":
            node=self.root
        ret=[]
        if node.getLHS() !="": # LHS가 존재한다면
            ret=ret+self.traverseInOrder(node.getLHS())
        if node.getRHS()!="":
            ret=ret+self.traverseInOrder(node.getRHS())
        ret.apppend(node.getValue())
        return ret

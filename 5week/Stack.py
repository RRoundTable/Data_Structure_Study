from ProductionList import ProductionList

# First-In_First_Out : 먼저 들어온거이 먼저 나간다. 놀이기구 줄서는 것과 유사한 원리

class Stack(ProductionList):
    def __init__(self):
        self.List = ProductionList('')

    def add(self, Object):
        # Problem 2. complete the add function of Stack
        # remember Stack has FIFO characteristics
        self.List.addFirst(Object)

    def get(self):
        # Problem 2. complete the remove function of Stack
        # remember Stack has FIFO characteristics
        Object = self.List.removeFirst()
        return Object

    def getSize(self):
        size = self.List.getSize()
        return size

    def getListString(self):
        string = self.List.getListString()
        return string
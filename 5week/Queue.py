from ProductionList import ProductionList

# Last-In_First_Out : 나중에 들어온 것이 먼저 나간다. 수식제어하는 프로그래밍에 쓰인다.


class Queue(ProductionList):
    def __init__(self):
        self.List = ProductionList('')

    def add(self, Object): # object : file?
        # Problem 3. complete the add function of Queue
        # remember Queue has LIFO characteristics
        self.List.addLast(Object)

    def get(self):
        # Problem 3. complete the remove function of Queue
        # % remember Queue has LIFO characteristics
        Object = self.List.removeFirst()
        return Object

    def getSize(self):
        size = self.List.getSize()
        return size

    def getListString(self):
        string = self.List.getListString()
        return string
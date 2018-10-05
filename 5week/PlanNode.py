class PlanNode: # linked list 구현하기
    def __init__(self, numNo, strSerialNumber, strModel, numModelNumber, dateStart, numAssemblyOrder, dateEnd,
                 strOrderOrigin):
        self.numNo = numNo
        self.strSerialNumber = strSerialNumber
        self.strModel = strModel
        self.numModelNumber = numModelNumber
        self.dateStart = dateStart
        self.numAssemblyOrder = numAssemblyOrder
        self.dateEnd = dateEnd
        self.strOrderOrigin = strOrderOrigin
        self.prevNode=None    # prevNode 생성하기
        self.nextNode=None   # nestNode 생성하기

    def printOut(self):
        print('No :', self.numNo, ', SerialNum : ', self.strSerialNumber, ',Model:', self.strModel, 'start date :',
              self.dateStart)

    def getNextNode(self):
        node = self.nextNode
        return node

    def getPrevNode(self):
        node = self.prevNode
        return node

    def setNextNode(self, node):
        # Problem 1. complete this method
        self.nextNode = node

    def setPrevNode(self, node):
        # Problem 1. complete this method
        self.prevNode = node
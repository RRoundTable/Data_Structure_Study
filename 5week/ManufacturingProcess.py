from Queue import Queue
from Stack import Stack

class ManufacturingProcess(Queue, Stack): # 제조 프로세스
    def __init__(self, typ):
        # setting waitingLine : Queue or Stack
        if typ == 'queue':
            self.waitingLine = Queue()
        if typ == 'stack':
            self.waitingLine = Stack()

    def arriveProduct(self, plan):
        self.waitingLine.add(plan)

    def leaveProduct(self):
        if self.getSize() > 0:
            plan = self.waitingLine.get() # get() : remove할 대상을 불러온다.
        else:
            plan = 'none' # none 설정해야 한다
        return plan

    def getSize(self):
        size = self.waitingLine.getSize() # Queue of Stack을 통해서 구현 ,
        return size

    def getListString(self):
        String = self.waitingLine.getListString()
        return String
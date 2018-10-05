import numpy as np
from ProductionList import ProductionList
from ManufacturingProcess import ManufacturingProcess
import matplotlib.pyplot as plt


class Factory(ManufacturingProcess):
    row = 2 # 무엇을 의미하는 변수인가1 : line
    col = 5 # 무엇을 의미하는 변수인가2 :  process
    numStartProduct = 2

    def __init__(self, strFilename, breakProb):
        self.breakProb = breakProb
        self.waitingProduct = ProductionList(strFilename) # waitingLine
        self.completedProduct = ProductionList('')

        # processes의 역할

        self.processes = [[[] for j in range(self.col)] for i in range(self.row)] # row*col matrix?
        for i in range(self.row):
            for j in range(self.col):
                # why ? 타입을 나누는 이유 찾기
                if i == 0: # 첫 번째 라인 : queue
                    self.processes[i][j] = ManufacturingProcess('queue')
                elif i == 1: # 두 번째 라인 : stack
                    self.processes[i][j] = ManufacturingProcess('stack')

    def selectLine(self, matCost):
        # Problem 1.
        # Return line = 1 or 2 by selecting a line by dynamic
        # programming. matCost = (Line) X (Processor)
        # Line = this.row
        # Processor = this.col
        # matcost : def getCostMatrix(self)의 return

        # Memoization table :  Storing the results of previous function calls to reuse the results again in the future(solution)
        matShortestCost = np.zeros((self.row, self.col))

        # Retrace table : 가는 경로 저장하기
        matPrevLine = np.zeros((self.row, self.col))

        # initialization of memoization table (the first col)
        for i in range(matShortestCost.shape[0]):
            matShortestCost[i][0] = matCost[i][0]
        # matShortestCost :
        # matCost :
        # dynamic programming iteration : matShortCost와 matPrevLine을 구한다
        for i in range(1,self.col): # col 은 num of stations을 의미한다.
            for j in range(self.row): # WaitingLine : node의 길이,  활용하기
                # process[j][i].getSize() node의 길이를
                if matShortestCost[0][i - 1] + matCost[j][i] < matShortestCost[1][i - 1] + matCost[j][i]:
                    matShortestCost[j][i] = matShortestCost[0][i - 1] + matCost[j][i]
                    matPrevLine[j][i] = int(0)
                else:
                    matShortestCost[j][i] = matShortestCost[1][i - 1] + matCost[j][i]
                    matPrevLine[j][i] = int(1)

        # choice of line by the dynamic programming
        if matShortestCost[0][self.col-1] < matShortestCost[1][self.col-1]:
            endLine = int(0)
        else:
            endLine = int(1)

        for i in range(self.col-1, 0, -1):
            endLine = int(matPrevLine[endLine][i])

        line = endLine

        print('======================')
        print('Cost Matrix : ')
        print(matShortestCost)
        print('Retrace Matrix : ')
        print(matPrevLine)
        return line

    def getCostMatrix(self): # MacturingProcess의 값중 하나
        matCost = np.zeros((self.row, self.col))
        for i in range(self.row):
            for j in range(self.col):
                matCost[i][j] = self.processes[i][j].getSize() # get waitingLine Size
                print("matCost : ",matCost)
        return matCost

    def run(self):
        cntProduct = self.waitingProduct.getSize()
        cntltr = 0
        while self.completedProduct.getSize() != cntProduct:
            fig = plt.figure()
            for j in range(self.numStartProduct):
                product = self.waitingProduct.removeFirst()
                if product != 'none':
                    line = self.selectLine(self.getCostMatrix())
                    print('S elected Line : ', line)
                    print('Product No. : ', product.numNo)
                    self.processes[line][0].arriveProduct(product)

            for jj in range(self.col):
                j = self.col - jj
                for i in range(self.row):
                    if j == self.col:

                        plt.text(100 + j * 50, 100, self.completedProduct.getListString(), style='italic')
                    else:
                        plt.text(100 + j * 50, 50 + i * 100, self.processes[i][j].getListString(), style='italic')

            for i in range(self.row):
                plt.text(100, 50 + i * 100, self.processes[i][0].getListString(), style='italic')

            plt.text(50, 100, self.waitingProduct.getListString(), style='italic')
            plt.axis([0, 450, 0, 200])
            plt.show()
            for jj in range(self.col):
                j = self.col - jj
                for i in range(self.row):
                    if self.breakProb < np.random.uniform(0, 1):
                        if j == self.col:
                            product = self.processes[i][j - 1].leaveProduct()
                            if product != 'none':
                                self.completedProduct.addLast(product)
                        else:
                            product = self.processes[i][j - 1].leaveProduct()
                            if product != 'none':
                                self.processes[i][j].arriveProduct(product)
            cntltr += 1

        fig = plt.figure()
        plt.text(100 + self.col * 50, 100, self.completedProduct.getListString(), style='italic')
        plt.axis([0, 450, 0, 200])
        plt.show()

        print('Count Iteration :', cntltr)

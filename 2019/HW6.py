import numpy as np
import matplotlib.pyplot as plt
import random

class Queue:
    def __init__(self):
        self.q =[]

    def enQueue(self, item):
        self.q.append(item)

    def deQueue(self):
        if self.isEmpty() == False:
            return self.q.pop(0)
        else :
            print("Empty queue!")

    def size(self):
        return len(self.que)

    def isEmpty(self):
        if len(self.q) > 0 :
            return False
        else :
            return True

    def peek(self):
        if self.isEmpty() == False:
            return self.q[0]
        else:
            print("Empty queue")

    def delete(self, item):
        if item in self.q:
            self.q.remove(item)
        else:
            print("No item in queue!")

class Customer:
    def __init__(self,arriveTime):
        self.arriveTime = arriveTime
        self.orderTime = None
        self.outTime = None

class Shop:
    def __init__(self):
        self.queue =[]

    def getSize(self):
        return len(self.queue)

    def entCust(self, Cust):
        self.queue.append(Cust)

    def outCust(self, currTime):
        while currTime >= self.queue[0].outTime:
            self.queue.pop(0)
            if len(self.queue) == 0:
                break

    def getLast(self):
        return self.queue[-1]

def main(lunchTime = False, employee = 1):
    coffeShop = Shop()
    currTime = 0
    cookTime = 1
    len_queue = []
    lamda = 1
    if lunchTime == True:
        intervals = np.random.exponential(lamda, 1000000)
        arriveTimes = np.cumsum(intervals)
        for idx in range(len(arriveTimes)):
            if  arriveTimes[idx] >= 4 * 60 and arriveTimes[idx] <= 6 * 60:
                lamda = 2
                intervals[idx] = np.random.exponential(lamda, 1)
    else:
        intervals = np.random.exponential(lamda, 1000000)
    arriveTimes = np.cumsum(intervals)
    for arriveTime in arriveTimes:
        if arriveTime >= 14 * 60:
            break
        Cust = Customer(arriveTime)
        if len(coffeShop.queue) <= employee - 1:
            Cust.orderTime = Cust.arriveTime
            Cust.outTime = Cust.orderTime + cookTime
        else:
            if coffeShop.queue[0].outTime > Cust.arriveTime:
                Cust.orderTime = coffeShop.queue[0].outTime + 1
                Cust.outTime = Cust.orderTime + cookTime
            else:
                Cust.orderTime = Cust.arriveTime
                Cust.outTime = Cust.orderTime + cookTime
        coffeShop.entCust(Cust)
        coffeShop.outCust(currTime)
        currTime = arriveTime
        len_queue.append(len(coffeShop.queue))
    return max(len_queue)


def result(iter = 100):
    basic =[]
    lunch = []
    employee2 =[]
    for i in range(iter):
        basic.append(main(lunchTime = False, employee = 1))
        lunch.append(main(lunchTime = True, employee = 1))
        employee2.append(main(lunchTime = False, employee = 2))
    basic_mean = np.mean(basic)
    lunch_mean = np.mean(lunch)
    employee2_mean = np.mean(employee2)
    print("basic : {} lunch : {} employee2 : {}".format(basic_mean, lunch_mean, employee2_mean))

result(100)
import numpy as np
import matplotlib.pyplot as plt

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
        if currTime >= self.queue[0].outTime:
            return self.queue.pop(0)

    def getLast(self):
        return self.queue[-1]


coffeShop = Shop()
currTime = 0
cookTime = 1

while currTime <= 14 * 80:
    interval = np.random.exponential(1, 1)
    arriveTime = currTime + interval
    Cust = Customer(arriveTime)

    if len(coffeShop.queue) == 0: # queue에 대기 손님이 없을 때
        Cust.orderTime = Cust.arriveTime
        Cust.outTime = Cust.orderTime + cookTime
    else:
        if coffeShop.queue[0].outTime > Cust.arriveTime:
            Cust.orderTime = coffeShop.queue[0].outTime
            Cust.outTime = Cust.orderTime + cookTime
        else:
            Cust.orderTime = Cust.arriveTime
            Cust.outTime = Cust.orderTime + cookTime


    coffeShop.entCust(Cust)
    coffeShop.outCust(currTime)
    print("queue의 길이 : {}".format(len(coffeShop.queue)))
    currTime += 1


# 큐의 최대 대기인원 : 9명
# 시간대 별로 도착시간 분포를 조정해 보세요
# 주문을 두 명이서 받는다면?


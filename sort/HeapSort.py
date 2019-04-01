import random
import time

N=100
lstNumbers=list(range(N))
random.seed(1)
random.shuffle(lstNumbers)

class MinHeap:
    def __init__(self):
        self.queue = [None]

    def parent(self, index):
        return int(index/2)

    def leftchild(self, index):
        return index * 2

    def rightchild(self, index):
        return index * 2 + 1

    def swap(self, x, y):
        """
        :param x: index
        :param y: index
        """
        tmp = self.queue[x]
        self.queue[x] = self.queue[y]
        self.queue[y] = tmp

    def insert(self, item):
        self.queue.append(item)
        i = len(self.queue) - 1
        while i > 1 :
            parent = self.parent(i)
            if self.queue[i] < self.queue[parent]:
                self.swap(i,parent)
                i = parent
            else :
                break

    # 최소값 제거
    def delete(self):
        self.swap(1,len(self.queue) - 1)
        item = self.queue.pop(len(self.queue) - 1)
        self.heapify(1)
        return item

    # 특정 index부터 heapify
    def heapify(self, index):
        left = self.leftchild(index)
        right = self.rightchild(index)
        smallest = index
        if left <= len(self.queue) - 1 and self.queue[left] < self.queue[smallest]:
            smallest = left
        if right <= len(self.queue) - 1 and self.queue[right] < self.queue[smallest]:
            smallest = right
        if smallest != index:
            self.swap(index, smallest)
            self.heapify(smallest) # recursive

def heapSort(lstNum) :
    """
    :param lstNum: 정렬되지 않은 list
    :return: 정렬된 list
    """
    result =[]
    minheap = MinHeap()
    for item in lstNum:
        minheap.insert(item)
    for _ in lstNum:
        result.append(minheap.delete())
    return result

print(heapSort(lstNumbers))



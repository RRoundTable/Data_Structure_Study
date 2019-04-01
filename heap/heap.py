import random

class Heap:
    """ Min heap"""

    def __init__(self):
        self.queue=[None]

    def parent(self, index):
        return int(index/2)

    def insert(self,n):
        self.queue.append(n)
        i=len(self.queue)-1
        while i>1:
            parent=self.parent(i)
            if self.queue[i]<self.queue[parent]:
                self.swap(i, parent) # 부모가 더 작게 바꿔준다
                i=parent
            else:
                break

    def swap(self,x,y):
        temp=self.queue[x]
        self.queue[x]=self.queue[y]
        self.queue[y]=temp

    def delete(self):
        self.swap(1,len(self.queue)-1) # 마지막 원소와 root를 바꿔준다
        self.queue.pop(len(self.queue)-1)
        self.heapify(1)

    def leftchild(self,index):
        return index*2

    def rightchild(self,index):
        return index*2+1

    def heapify(self,i):
        left=self.leftchild(i)
        right=self.rightchild(i)
        smallest=i
        if left<=len(self.queue)-1 and self.queue[left]< self.queue[smallest]:
            smallest=left
        if right<=len(self.queue)-1 and self.queue[right]<self.queue[smallest]:
            smallest=right
        if smallest!=i:
            self.swap(i, smallest)
            self.heapify(smallest)

minheap=Heap()
for _ in range(100):
    minheap.insert(random.randint(1,50))

print(minheap.queue)
for _ in range(10):
    minheap.delete()

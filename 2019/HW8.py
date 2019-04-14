class BinaryTree:
    def __init__(self):
        self.t = [None]

    def append(self, item):
        self.t.append(item)

    def size(self):
        return len(self.t) - 1

    def getChild(self, item):
        if item in self.t:
            k = self.t.index(item)
            lidx = 2 * k
            ridx = 2 * k + 1

            if lidx <= self.size():
                lnode= self.t[lidx]
            else:
                lnode = None
            if ridx <= self.size():
                rnode = self.t[ridx]
            else:
                rnode = None
            return lnode, rnode
        else:
            print("item not found ~")

    def getParent(self, item):
        if item in self.t:
            k = self.t.index(item)
            pidx = k // 2 # 1 or 0
            if pidx > 0:
                return self.t[pidx]
            else:
                return self
        else:
            print("item not found ~")
            return None

    def get_level(self, item):
        count = 0
        tmp = item
        while True:
            tmp = self.getParent(tmp)
            count += 1
            if tmp == self.t[1]:
                return count
            if tmp == None:
                return 0

    def get_distance(self, a, b):
        # 같은 부모를 찾는데 걸리는 경로
        while True:
            a_p = self.getParent(a)
            b_p = self.getParent(b)
            if a_p == None:
                break
            if a_p == b_p:
                level = self.get_level(a_p) # 잘못된 item
                return (3 - level) * 1/3
                break
            else:
                a = a_p
                b = b_p





disease = ['호흡기/소화기병', '호흡기병', '소화기병', '호흡기감염', '폐질환',
           '위질환', '결장질환', '독감', '기관지염', '폐부종', '폐색전증', '위궤양', '위암', '대장염', '대장암']

t = BinaryTree()

for d in disease:
    t.append(d)



print(t.get_level('독감'))
print(t.get_distance('대장염', '대장암'))
print(t.get_distance('대장염', '위궤양'))
print(t.getParent('대장염'))
print(t.get_distance('대장염', '기관지염'))
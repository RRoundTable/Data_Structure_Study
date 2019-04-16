class Node:
    def __init__(self, x):
        self.x = x
        self.r = None
        self.l = None


class Tree:
    def __init__(self, numbers, target):
        self.queue = []
        self.numbers = numbers
        self.root = None
        self.target = target

    def insert(self, item, i, node=None):
        if self.root == None:
            self.root = Node(0)
        if node == None:
            node = self.root
        if node.l is not None and node.r is not None:
            if node.r.x != 'stop':
                self.insert(item, i, node.r)
            if node.l.x != 'stop':
                self.insert(item, i, node.l)
        if node.r is None:
            if node.x + sum(self.numbers[i:]) < self.target:
                node.r = Node('stop')
            else:
                node.r = Node(node.x + eval('+' + str(item)))
                if i + 1 == len(self.numbers):
                    self.queue.append(node.r.x)
        if node.l is None:
            if node.x - sum(self.numbers[i:]) > self.target:
                node.l = Node('stop')
            else:
                node.l = Node(node.x + eval('-' + str(item)))
                if i + 1 == len(self.numbers):
                    self.queue.append(node.l.x)


def solution(numbers, target):
    answer = 0  # the number of solutions
    num_len = len(numbers)
    numbers = sorted(numbers, reverse=True)
    tree = Tree(numbers, target)
    i = 0
    for n in numbers:
        tree.insert(n, i)
        i += 1
    return tree.queue.count(target)
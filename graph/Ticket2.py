

class Node:
    def __init__(self, x, graph):
        self.x = x
        self.child = None
        self.graph = graph

class Tree:
    def __init__(self):
        self.root = None
        self.queue = []
    def insert(self, key, graph=None, node=None):
        if self.root == None:
            self.root = Node(key, graph)
        if node == None:
            node = self.root
        if graph == None:
            graph = node.graph
        if node.child is None:
            for i in graph[key]:
                tmp = graph.copy()
                if node.child is None:
                    idx = tmp[key].index(i)
                    if idx + 1 < len(tmp[key]):
                        tmp[key] = tmp[key][:idx] + tmp[key][idx +1:]
                    else:
                        tmp[key] = tmp[key][:idx]
                    node.child = [Node(i, tmp)]
                    if tmp[i] is None:
                        return
                    if len(tmp[i]) > 0:
                        self.insert(i, tmp, node.child[0])
                    else:
                        print("END")
                else:
                    idx = tmp[key].index(i)
                    if idx + 1 < len(tmp[key]):
                        tmp[key] = tmp[key][:idx] + tmp[key][idx +1:]
                    else:
                        tmp[key] = tmp[key][:idx]
                    node.child.append(Node(i, tmp))
                    if tmp[i] is None:
                        return
                    if len(tmp[i]) > 0:
                        self.insert(i, tmp, node.child[-1])
                    else:
                        print("END")

    def print_paths(self, root):
        path = []
        return self.print_paths_rec(root, path, 0)

    def print_paths_rec(self, root, path, pathLen, result = None):
        if root is None:
            return
        if result is None:
            result = []

        if len(path) > pathLen:
            path[pathLen] = root.x
        else:
            path.append(root.x)

        pathLen += 1

        if root.child is None:
            result.append(self.print_array(path, pathLen))
        else:
            for c in root.child:
                self.print_paths_rec(c, path, pathLen, result)
        return result

    def print_array(self, ints, len):
        result = []
        for i in ints:
            result.append(i)
        return result

def solution(tickets):
    graph = {}
    for i in range(len(tickets)):
        try:
            graph[tickets[i][0]].append(tickets[i][1])
        except:
            graph[tickets[i][0]] = [tickets[i][1]]
    keys = graph.keys()
    remain = set([g for s, g in tickets]) - set(keys)
    for r in remain:
        graph[r] = None
    tree = Tree()
    tree.insert('ICN', graph)
    result = tree.print_paths(tree.root)
    result = [ r for r in result if len(r) == len(tickets ) +1]
    order = []
    for i in range(len(result)):
        alphabet = ""
        for j in result[i]:
            alphabet += j[0]
        order.append(alphabet)
    
    result = sorted(result, key = (lambda x : order[result.index(x)]))
    return result[0]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
print(solution(tickets))
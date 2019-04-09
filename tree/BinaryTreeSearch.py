from TreeNode import TreeNode

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value, node = None):
        """
        :param value: insert 할 value
        :param node: insert할 위치
        """
        if self.root == None:
            self.root = TreeNode(value, None)
            return

        if node == None:
            node = self.root

        if node.value > value:
            if node.getLHS() == None:
                node.setLHS(TreeNode(value, node))
                node.getLHS().set_parent(node) # setting parent node
            else:
                self.insert(value, node.getLHS())

        elif node.value < value:
            if node.getRHS() == None:
                node.setRHS(TreeNode(value, node))
                node.getRHS().set_parent(node)
            else:
                self.insert(value, node.getRHS())

    def search(self, value, node = None):
        if node == None:
            node = self.root

        if value == node.get_value():
            return True

        if value > node.get_value():
            if node.getRHS() == None:
                return False
            else:
                return self.search(value, node.getRHS())
        if value < node.get_value():
            if node.getLHS() == None:
                return False
            else:
                return self.search(value, node.getLHS())

    def delete(self, value):
        self.root, deleted = self.delete_value(self.root, value)
        return deleted

    def delete_value(self, node , value):
        """
        :param node:
        :param value:
        :return: self.root, deleted(T/F)
        """
        if node == None:
            return node, False

        deleted = False
        if value == node.value:
            deleted = True
            if node.getLHS() != None and node.getRHS() != None:
                parent, child = node, node.getRHS()
                while child.getLHS() != None:
                    parent, child = child, child.getLHS()
                child.setLHS(node.getLHS())
                if parent != node:
                    parent.setLHS(child.getRHS())
                    child.setRHS(node.getRHS())
                node = child
        elif value < node.value:
            nodeLHS, deleted = self.delete_value(node.getLHS(), value)
        else:
            nodeRHS, deleted = self.delete_value(node.getRHS(), value)
        return node, deleted


    def find_min(self, node):
        if node == None:
            node = self.root
        if node.getLHS() == None:
            return node
        else:
            self.find_min(node.getLHS())

    def find_max(self, node):
        if node == None:
            node = self.root
        if node.getRHS() == None:
            return node
        else:
            self.find_max(node.getRHS())
    ########################
    # depth first traversal#
    def pre_order_traversal(self, node = None):

        if node == None:
            node = self.root

        ret = []
        ret.append(node.value)

        if node.getLHS() != None:
            ret += self.pre_order_traversal(node.getLHS())
        if node.getRHS() != None:
            ret += self.pre_order_traversal(node.getRHS())
        return ret

    def post_order_traversal(self, node = None):
        if node == None:
            node = self.root

        ret = []
        if node.getLHS() != None:
            ret += self.pre_order_traversal(node.getLHS())
        if node.getRHS() != None:
            ret += self.pre_order_traversal(node.getRHS())
        ret.append(node.value)
        return ret

    def in_order_traversal(self, node=None):
        if node == None:
            node = self.root
        ret = []
        if node.getLHS() != None:
            ret += self.pre_order_traversal(node.getLHS())
        ret.append(node.value)
        if node.getRHS() != None:
            ret += self.pre_order_traversal(node.getRHS())
        return ret
    ##########################
    # breadth first traversal#
    def level_order_traversal(self, node = None):
        if node == None:
            node = self.root
        ret = []
        queue = [node]
        while queue:
            root = queue.pop(0)
            if root is not None:
                ret.append(root.value)
                if root.getLHS() != None:
                    queue.append(root.getLHS())
                if root.getRHS() != None:
                    queue.append(root.getRHS())
        return ret


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

print(bst.search(15)) # True
print(bst.search(17)) # False

# depth first
print(bst.pre_order_traversal())   # 40 4 34 14 13 15 45 55 48 47 49
bst.in_order_traversal()    # 4 13 14 15 34 40 45 47 48 49 55
bst.post_order_traversal()  # 13 15 14 34 4 47 49 48 55 45 40
# breadth first
bst.level_order_traversal() # 40 4 45 34 55 14 48 13 15 47 49

bst.delete(55) # True

# depth first
bst.pre_order_traversal()   # 40 4 34 14 13 15 45 48 47 49
bst.in_order_traversal()    # 4 13 14 15 34 40 45 47 48 49
bst.post_order_traversal()  # 13 15 14 34 4 47 49 48 45 40
# breadth first
bst.level_order_traversal() # 40 4 45 34 48 14 47 49 13 15

bst.delete(14) # True

# depth first
bst.pre_order_traversal()   # 40 4 34 15 13 45 48 47 49
bst.in_order_traversal()    # 4 13 15 34 40 45 47 48 49
bst.post_order_traversal()  # 13 15 34 4 47 49 48 45 40
# breadth first
bst.level_order_traversal() # 40 4 45 34 48 15 47 49 13

bst.delete(11) # False

# depth first
bst.pre_order_traversal()   # 40 4 34 15 13 45 48 47 49
bst.in_order_traversal()    # 4 13 15 34 40 45 47 48 49
bst.post_order_traversal()  # 13 15 34 4 47 49 48 45 40
# breadth first
bst.level_order_traversal() # 40 4 45 34 48 15 47 49 13
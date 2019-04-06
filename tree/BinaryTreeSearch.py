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


array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.search(15)) # True
print(bst.search(17)) # False

# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False
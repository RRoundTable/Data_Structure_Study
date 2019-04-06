
class TreeNode:

    def __init__(self, value, node_parent):
        self.value = value
        self.node_parent = node_parent
        self.nodeLHS = None
        self.nodeRHS = None
        self.value = value

    def getLHS(self):
        return self.nodeLHS

    def getRHS(self):
        return self.nodeRHS

    def setLHS(self, LHS):
        self.nodeLHS = LHS

    def setRHS(self, RHS):
        self.nodeRHS = RHS

    def set_value(self, value):
        self.value = value

    def set_parent(self, parent):
        self.node_parent = parent

    def get_value(self):
        return self.value
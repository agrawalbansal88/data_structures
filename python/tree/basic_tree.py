class Node():
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None

class Tree():
    def __init__(self):
        self.root = None

    def bulk_insert(self, datas):
        for data in datas:
            self.insert(data)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, root):
        if root is None:
            root = Node(data)
            return

        if root.data > data:
            if root.l is not None:
                self._insert(data, root.l)
            else:
                root.l = Node(data)
        elif root.data < data:
            if root.r is not None:
                self._insert(data, root.r)
            else:
                root.r = Node(data)

    # Left - Root - Right
    # Inorder traversal gives nodes in non-decreasing order
    def printInorder(self, node):
        if(node!=None):
            self.printInorder(node.l)
            print(node.data)
            self.printInorder(node.r)

    # Root - Left - Right
    # Preorder traversal is used to create a copy of the tree.
    def printPreorder(self, node):
        if(node!=None):
            print(node.data)
            self.printInorder(node.l)
            self.printInorder(node.r)

    # Left - Right - Root
    # Postorder traversal is used to delete the tree
    def printPostorder(self, node):
        if(node!=None):
            self.printInorder(node.l)
            self.printInorder(node.r)
            print(node.data)

tree = Tree()

tree.insert(10)
tree.insert(11)
tree.insert(12)
tree.insert(8)
tree.insert(7)
tree.bulk_insert([1,5,7,-11, 11])
tree.printInorder(tree.root);print "\n"
tree.printPreorder(tree.root);print "\n"
tree.printPostorder(tree.root);print "\n"

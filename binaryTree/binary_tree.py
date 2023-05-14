
from Node import TreeNode
class BinaryTree:
    def __init__(self, value) -> None:
        self.root: TreeNode = TreeNode(value)

    def preOrder(self, node: TreeNode):
        if node is not None:
            print(node)
            self.preOrder(node.left)
            self.preOrder(node.rigth)
            
    def inOrder(self, node: TreeNode):
        if node is not None:
            self.inOrder(node.left)
            print(node)
            self.inOrder(node.rigth)
            
    def postOrder(self, node: TreeNode):
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.rigth)
            print(node)
            

    def __str__(self) -> str:
        return f"{self.root}"
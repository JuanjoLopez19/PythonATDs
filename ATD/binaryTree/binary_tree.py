
from ATD.binaryTree.Node import TreeNode
class BinaryTree:
    def __init__(self, value) -> None:
        self.root: TreeNode = TreeNode(value)
    
    def  insert(self, value:str) -> int:
        if self.root is None:
            self.root = TreeNode(value)
            return 0
        else:
            temp: list[TreeNode] = [self.root]
            while temp is not None:
                temp_node: TreeNode = temp.pop(0)
                if temp_node.left is None:
                    temp_node.left = TreeNode(value)
                    return 0
                elif temp_node.rigth is None:
                    temp_node.rigth = TreeNode(value)
                    return 0
                else:
                    temp.append(temp_node.left)
                    temp.append(temp_node.rigth)
                

                    

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
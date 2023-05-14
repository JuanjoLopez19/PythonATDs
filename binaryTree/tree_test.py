from binary_tree import BinaryTree
from Node import TreeNode
aux: BinaryTree = BinaryTree("a")

aux.root.left = TreeNode("d")
aux.root.rigth = TreeNode("x")
aux.root.rigth.rigth = TreeNode(2)
aux.root.rigth.rigth.left = TreeNode("dasd")

aux.inOrder(aux.root)
from ATD.binaryTree.binary_tree import BinaryTree
aux: BinaryTree = BinaryTree("a")

aux.insert("b")
aux.insert("c")
aux.insert("d")
aux.insert("e")
aux.insert("f")
aux.insert("g")




if __name__ == '__main__':
    aux.inOrder(aux.root)

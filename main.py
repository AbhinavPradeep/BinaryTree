from Tree import BinaryTree
from Node import Node

def printTree(node:Node, level=0):
    if node != None:
        printTree(node.LeftNode, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.Value))
        printTree(node.RightNode, level + 1)

Tree = BinaryTree()

Tree.RecursiveInsert(10)

Tree.RecursiveInsert(12)

Tree.RecursiveInsert(8)

Tree.RecursiveInsert(16)

Tree.RecursiveInsert(14)

Tree.RecursiveInsert(5)

Tree.RecursiveInsert(6)

Tree.RecursiveInsert(7)

Tree.RecursiveInsert(3)

Tree.RecursiveInsert(10)

Tree.RecursiveInsert(11)

#Tree.Insert(10.5)

Tree.RecursiveInsert(10.5)

# for i in  range(10):
#     Tree.Insert(i)

printTree(Tree.HeadNode)

print(Tree.HeadNode)
# Tree.Delete(6)

# print("\n")

# print(Tree.Search(14))

# print("\n")

# printTree(Tree.HeadNode)

# print("\n")

# Tree.InOrderTraversal(Tree.HeadNode)

# print("\n")

# Tree.PreOrderTraversal(Tree.HeadNode)
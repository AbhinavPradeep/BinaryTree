from Node import Node
class BinaryTree:
    def __init__(self) -> None:
        self.HeadNode = None

    def Insert(self,ValueToInsert:int) -> None:
        if self.HeadNode == None:
            self.HeadNode = Node(ValueToInsert)
        else:
            CurrentNode = self.HeadNode
            Inserted = False
            while Inserted == False:
                if ValueToInsert > CurrentNode.Value and CurrentNode.RightNode == None:
                    CurrentNode.RightNode = Node(ValueToInsert)
                    Inserted  = True
                elif ValueToInsert <= CurrentNode.Value and CurrentNode.LeftNode == None:
                    CurrentNode.LeftNode = Node(ValueToInsert)
                    Inserted = True
                elif ValueToInsert > CurrentNode.Value and CurrentNode.RightNode != None:
                    CurrentNode = CurrentNode.RightNode
                elif ValueToInsert <= CurrentNode.Value and CurrentNode.LeftNode != None:
                    CurrentNode = CurrentNode.LeftNode
    
    def RecursiveInsert(self,ValueToInsert:int,Subtree=None):
        if self.HeadNode == None:
                self.HeadNode = Node(ValueToInsert)
        else:
            if Subtree == None:
                Subtree = self.HeadNode
            if ValueToInsert > Subtree.Value and Subtree.RightNode != None:
                self.RecursiveInsert(ValueToInsert,Subtree.RightNode)
            elif ValueToInsert <= Subtree.Value and Subtree.LeftNode != None:
                self.RecursiveInsert(ValueToInsert,Subtree.LeftNode)
            if ValueToInsert > Subtree.Value and Subtree.RightNode == None:
                Subtree.RightNode = Node(ValueToInsert)
            elif ValueToInsert <= Subtree.Value and Subtree.LeftNode == None:
                Subtree.LeftNode = Node(ValueToInsert)
    
    def Search(self,ValueToBeFound) -> Node|None:
        if self.HeadNode == None:
            return None
        else:
            CurrentNode = self.HeadNode
            EndReached = False
            ReturnNode = None
            while EndReached == False:
                if ValueToBeFound > CurrentNode.Value and CurrentNode.RightNode != None:
                    CurrentNode = CurrentNode.RightNode
                elif ValueToBeFound < CurrentNode.Value and CurrentNode.LeftNode != None:
                    CurrentNode = CurrentNode.LeftNode
                elif (ValueToBeFound > CurrentNode.Value and CurrentNode.RightNode == None) or (ValueToBeFound < CurrentNode.Value and CurrentNode.LeftNode == None):
                    EndReached = True
                elif CurrentNode.Value == ValueToBeFound:
                    ReturnNode = CurrentNode
                    EndReached = True
            return ReturnNode


    def Delete(self,ValueToBeDeleted) -> None:
        if self.HeadNode == None:
            return None
        else:
            CurrentNode = self.HeadNode
            EndReached = False
            while EndReached == False:
                if CurrentNode.RightNode != None and ValueToBeDeleted > CurrentNode.RightNode.Value:
                    CurrentNode = CurrentNode.RightNode
                elif CurrentNode.LeftNode != None and ValueToBeDeleted < CurrentNode.LeftNode.Value:
                    CurrentNode = CurrentNode.LeftNode
                elif CurrentNode.LeftNode == None and ValueToBeDeleted > CurrentNode.Value:
                    CurrentNode = CurrentNode.RightNode
                elif CurrentNode.RightNode == None and ValueToBeDeleted < CurrentNode.Value:
                    CurrentNode = CurrentNode.LeftNode
                elif (ValueToBeDeleted > CurrentNode.Value and CurrentNode.RightNode == None) or (ValueToBeDeleted < CurrentNode.Value and CurrentNode.LeftNode == None):
                    EndReached = True
                if CurrentNode.RightNode != None and CurrentNode.RightNode.Value == ValueToBeDeleted:
                    RightTree = CurrentNode.RightNode.RightNode
                    LeftTree = CurrentNode.RightNode.LeftNode
                    CurrentNode.RightNode = RightTree
                    CurrentNode = CurrentNode.RightNode
                    while CurrentNode.LeftNode != None:
                         CurrentNode = CurrentNode.LeftNode
                    CurrentNode.LeftNode = LeftTree
                    #CurrentNode.RightNode = None
                    EndReached = True
                elif CurrentNode.LeftNode != None and CurrentNode.LeftNode.Value == ValueToBeDeleted:
                    RightTree = CurrentNode.LeftNode.RightNode
                    LeftTree = CurrentNode.LeftNode.LeftNode
                    CurrentNode.LeftNode = RightTree
                    CurrentNode = CurrentNode.LeftNode
                    while CurrentNode.LeftNode != None:
                         CurrentNode = CurrentNode.LeftNode
                    CurrentNode.LeftNode = LeftTree
                    #CurrentNode.LeftNode = None
                    EndReached = True

    def InOrderTraversal(self,node: Node):
        if node.LeftNode != None:
        #    print("L")
            self.InOrderTraversal(node.LeftNode)
        #print("E")
        print(node.Value)
        if node.RightNode != None:
        #    print("R")
            self.InOrderTraversal(node.RightNode)

    def PreOrderTraversal(self,node: Node):
        print(node.Value)
        if node.LeftNode != None:
        #    print("L")
            self.InOrderTraversal(node.LeftNode)
        if node.RightNode != None:
        #    print("R")
            self.InOrderTraversal(node.RightNode)

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.NumNode=0

    #Helper function of insetBST
    def insertHelper(self,root,data):
        if root is None:
            NewNode=BinaryTreeNode(data)
            return NewNode

        if root.data>data:
            root.left=self.insertHelper(root.left,data)
            return root
        else:
            root.right=self.insertHelper(root.right,data)
            return root


    #Insert in BST
    def insertBST(self,data):
        self.NumNode = self.NumNode + 1
        self.root=self.insertHelper(self.root,data)



    def printTreeHelper(self,root):
        if root is None:
            return
        print(root.data,end=":")
        if root.left is not None:
            print(root.left.data,end=",")
        if root.right is not None:
            print(root.right.data,end="")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)



    #Helper function of isPresent
    def isPresentHelper(self,root,data):
        if root is None:
            return False
        if root.data==data:
            return True
        if root.data>data:
            return self.isPresentHelper(root.left,data)
        else:
            return self.isPresentHelper(root.right,data)

    #Check data is present or not
    def isPresent(self,data):
        return self.isPresentHelper(self.root,data)




    #Get the minimun node in BST
    def min(self,root):
        if root is None:
            return 10000000
        if root.left is None:
            return root.data
        return self.min(root.left)


   #Helper funcction of DeleteData
    def deleteHelper(self,root,data):
        if root is None:
            return False,None
        if root.data<data:
            deleted,newRightNode=self.deleteHelper(root.right,data)
            root.right=newRightNode
            return deleted,root
        if root.data>data:
            deleted,newLeftNode=self.deleteHelper(root.left,data)
            root.left=newLeftNode
            return deleted,root

        #root has no child
        if root.left is None and root.right is None:
            return True,None

        #root has one child
        if  root.left is None:
            return True,root.right
        #root has one child
        if root.right is  None:
            return True,root.left

        #root has two  child
        if root.left is not None and root.right is not None:
            replacement=self.min(root.right)
            root.data=replacement
            deleted,newRightNode=self.deleteHelper(root.right,replacement)
            root.right=newRightNode
            return True,root

    def deleteData(self,data):
        if self.root is None:
            return
        deleted,NewNode=self.deleteHelper(self.root,data)
        if deleted:
            self.NumNode-=1
            return deleted

    def count(self):
        return self.NumNode

b=BST()
b.insertBST(10)
b.insertBST(5)
b.insertBST(7)
b.insertBST(6)
b.insertBST(8)
b.insertBST(12)
b.insertBST(11)
b.insertBST(15)

print(b.isPresent(15))


b.printTree()


print(b.count())


print(b.deleteData(10))

b.printTree()


print(b.count())



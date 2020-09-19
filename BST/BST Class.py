class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None





class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    #-----------------------------------------#
    def printTreeHelper(self, root):
        if root is None:
            return
        print(root.data,end=":")
        if root.left is not None:
            print("L:",end="")
            print(root.left.data,end=",")
        if root.right is not None:
            print("R:",end="")
            print(root.right.data,end="")
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)
    #-----------------------------------------#

    #-----------------------------------------#
    def isPresent(self,root,data):
        if root is None:
            return False

        if root.data==data:
            return True

        if root.data>data:
            return self.isPresent(root.left,data)
        if root.data<data:
            return self.isPresent(root.right,data)

    def search(self, data):
        return self.isPresent(self.root,data)
    #-----------------------------------------#


    #-----------------------------------------#
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

    def insert(self, data):
        self.numNodes+=1
        self.root = self.insertHelper(self.root, data)

    #-----------------------------------------#


    #-----------------------------------------#

    def min(self,root):
        if root is None:
            return 10000000
        if root.left is None:
            return root.data
        return self.min(root.left)

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

    def delete(self, data):
        deleted,NewNode=self.deleteHelper(self.root,data)
        if deleted:
            self.numNodes-=1
            return True,deleted
        else:
            return False,None


    # -----------------------------------------#

    def count(self):
        return self.numNodes


b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while (i < (len(li))):
    choice = li[i]
    if choice == 1:
        data = li[i + 1]
        b.insert(data)
        i += 2
    elif choice == 2:
        data = li[i + 1]
        b.delete(data)
        i += 2
    elif choice == 3:
        data = li[i + 1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i += 2
    else:
        b.printTree()
        i += 1


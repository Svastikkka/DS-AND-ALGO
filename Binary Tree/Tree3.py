class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printTree(root):
    if root is None:
        return
    print(root.data,end=":")
    if root.left is not None:
        print("L:",root.left.data,end=",")
    if root.right is not None:
        print("R:",root.right.data,end="")
    print()
    printTree(root.left)
    printTree(root.right)
def inputTree():
    data=int(input()) #taking input
    if data is -1:
        return
    root=BinaryTreeNode(data) # creating a node
    root.left=inputTree()
    root.right=inputTree()
    return root

printTree(inputTree())


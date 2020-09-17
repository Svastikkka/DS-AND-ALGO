class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inputTree():
    data=int(input())
    if data is -1:
        return
    root=BinaryTreeNode(data)
    root.left=inputTree()
    root.right=inputTree()
    return root




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


def NodeSum(root):
    if root is None:
        return 0
    rootCount=root.data
    leftCount=NodeSum(root.left)
    rightCount=NodeSum(root.right)
    return rootCount+leftCount+rightCount

printTree(inputTree())
#print(NodeSum(root))
#5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1

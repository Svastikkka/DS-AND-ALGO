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

def countNodesGreaterThanX(root,x):
    if root is None:
        return 0

    leftNode=countNodesGreaterThanX(root.left,x)
    rightNode=countNodesGreaterThanX(root.right,x)
    if root.data>x:
        return 1+leftNode+rightNode
    return leftNode+rightNode



def preOrder(root):
    if root is None:
        return
    print(root.data,end=":")
    if root.left is not None:
        print(root.left.data,end=",")
    if root.right is not  None:
        print(root.right.data,end="")
    print()
    preOrder(root.left)
    preOrder(root.right)

#preOrder(inputTree())
print(countNodesGreaterThanX(inputTree(),int(input())))

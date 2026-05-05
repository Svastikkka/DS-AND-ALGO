"""
Root To Node Path In Binary Tree
"""
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inputBST(arr):
    if len(arr)==0:
        return
    midIndex=(len(arr)-1)//2
    root=BinaryTreeNode(arr[midIndex])
    root.left=inputBST(arr[0:midIndex])
    root.right=inputBST(arr[midIndex+1:])
    return root

def preOrder(root):
    if root is None:
        return None
    print(root.data,end=" ")
    if root.left is not None:
        print(root.left.data,end=",")
    if root.right is not None:
        print(root.right.data,end="")
    print()
    preOrder(root.left)
    preOrder(root.right)


def nodeToRootPath(root,s):
    if root is None:
        return None
    if root.data==s:
        l=[]
        l.append(root.data)
        return l
    leftOutput=nodeToRootPath(root.left,s)
    if leftOutput is not None:
        leftOutput.append(root.data)
        return leftOutput
    rightOutput=nodeToRootPath(root.right,s)
    if rightOutput is not None:
        rightOutput.append(root.data)
        return rightOutput
    else:
        return None

arr=list(map(int,input().split()))
preOrder(inputBST(arr))
print(nodeToRootPath(inputBST(arr),5))
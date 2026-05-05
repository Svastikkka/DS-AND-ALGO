"""Check It IS bst or not"""
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
def minTree(root):
    if root is None:
        return -10000000
    leftMin=minTree(root.left)
    rightMin=minTree(root.right)
    return max(leftMin,rightMin,root.data)
def maxTree(root):
    if root is None:
        return -10000000
    leftMax=maxTree(root.left)
    rightMax=maxTree(root.right)
    return max(leftMax,rightMax,root.data)

def isBst(root):
    if root is None:
        return True

    leftMax=maxTree(root.left)
    rightMin=minTree(root.right)
    if root.data>rightMin and root.data<=leftMax:
        return False
    leftBST=isBst(root.left)
    rightBST=isBst(root.right)
    return leftBST and rightBST

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

arr=list(map(int,input().split()))
print(isBst(inputBST(arr)))

class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inputBST(arr):
    if len(arr)==0:
        return
    mid=(len(arr)-1)//2
    root=BinaryTreeNode(arr[mid])
    root.left=inputBST(arr[0:mid])
    root.right=inputBST(arr[mid+1:])
    return root
def isBST(root,min,max):
    if root is None:
        return True
    if root.data<min or root.data>max:
        return False
    isLeftWithInConstraint=isBST(root.left,min,root.data-1)
    isRightWithInConstraint=isBST(root.right,root.data,max)

    return isLeftWithInConstraint and isRightWithInConstraint

arr=list(map(int,input().split()))
print(isBST(inputBST(arr),-10000000,10000000))
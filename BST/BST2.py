
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inputBST(arr):
    if len(arr)==0:
        return
    lenght=len(arr)

    mid=(lenght-1)//2
    root=BinaryTreeNode(arr[mid])
    root.left=inputBST(arr[0:mid])
    root.right=inputBST(arr[mid+1:])


    return root


def bst2(root):
    if root is None:
        return 1000000,-1000000,True
    leftMin,leftMax,isLeftBst=bst2(root.left)
    rightMin,rightMax,isRightBst=bst2(root.right)

    minimum=min(leftMin,rightMin,root.data)
    maximum=max(leftMax,rightMax,root.data)

    isTreeBST=True
    if root.data<=leftMax or root.data>rightMin:
        isTreeBST=False
    if not(isLeftBst) or not(isRightBst):
        isTreeBST=False
    return minimum,maximum,isTreeBST


arr=list(map(int,input().split()))
print(bst2(inputBST(arr)))



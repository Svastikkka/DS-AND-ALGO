import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePreOrder(preorder, inorder):
    if len(preorder)==0 or len(inorder)==0:
        return None

    rootData=preorder[0]
    root=BinaryTreeNode(rootData)


    rootIndexInOrder=-1
    for i in range(0,len(inorder)):
        if inorder[i]==rootData:
            rootIndexInOrder=i
            break
    if rootIndexInOrder ==-1:
        return None

    leftInOrder=inorder[0:rootIndexInOrder]
    rightInOrder=inorder[rootIndexInOrder+1:]

    lenOfLeft=len(leftInOrder)

    leftPreOrder=preorder[1:lenOfLeft+1]
    rightPreOrder=preorder[lenOfLeft+1:]

    leftChild=buildTreePreOrder(leftPreOrder,leftInOrder)
    rightChild=buildTreePreOrder(rightPreOrder,rightInOrder)

    root.left=leftChild
    root.right=rightChild
    return root










def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
n=int(input())
preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePreOrder(preorder, inorder)
printLevelATNewLine(root)

import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
    if len(postorder)==0:
        return None
    rootData=postorder[len(postorder)-1]
    root=BinaryTreeNode(rootData)

    rootIndexInOrder=-1

    for i in range(0,len(inorder)):
        if rootData==inorder[i]:
            rootIndexInOrder=i
            break
    if rootIndexInOrder==-1:
        return None
    #Slicing  InOrder
    leftInOrder=inorder[0:rootIndexInOrder]
    rightInOrder=inorder[rootIndexInOrder+1:]

    #Length
    lengthOfLeftInOrder=len(leftInOrder)

    #Slicing PostOrder
    leftPostOrder=postorder[0:lengthOfLeftInOrder]
    rightPostOrder=postorder[lengthOfLeftInOrder:len(postorder)-1]

    #Recursion
    root.left=buildTreePostOrder(leftPostOrder,leftInOrder)
    root.right=buildTreePostOrder(rightPostOrder,rightInOrder)



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
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)








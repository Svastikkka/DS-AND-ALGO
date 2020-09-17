import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesWithoutSibling(root):
    # Given a binary tree, print all nodes that don’t have a sibling. Print the
    # elements in different lines. And order of elements doesn't matter.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return
    # If this is an internal node , recur for left
    # and right subtrees
    if root.left is not None and root.right is not None:
        nodesWithoutSibling(root.left)
        nodesWithoutSibling(root.right)

        # If left child is NULL, and right is not, print
    # right child and recur for right child
    elif root.right is not None:
        print(root.right.data)
        nodesWithoutSibling(root.right)

        # If right child is NULL and left is not, print
    # left child and recur for left child
    elif root.left is not None:
        print(root.left.data)
        nodesWithoutSibling(root.left)

    #nodesWithoutSibling(root.right)
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
nodesWithoutSibling(root)

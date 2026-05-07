class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(2)
btn3=BinaryTreeNode(3)
btn4=BinaryTreeNode(4)
btn5=BinaryTreeNode(5)

"""Assigning the lef and right nodes """
btn1.left=btn2
btn1.right=btn3
btn2.left=btn4
btn2.right=btn5

print(btn1.data,btn1.left,btn1.right)
print(btn1.data,btn1.left.data,btn1.right.data)
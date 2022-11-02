
'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the postorder traversal of the tree.
def tra(root,x):
    if root is None:
        return
    tra(root.left,x)
    tra(root.right,x)
    x.append(root.data)
    
def postOrder(root):
    # code here
     x = []
     tra(root,x)
     return x


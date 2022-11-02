'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case

def isleaf(root):
    if root.left is None and root.right is None:
        return True
    return False
    
def tra(root,x):
    if root==None:
        pass
    elif isleaf(root):
        x.append(1)
    else:
        tra(root.left,x)
        tra(root.right,x)
    
def countLeaves(root):
    # Code here
    if root is None:
        return -1
    x = []
    tra(root,x)
    return len(x)


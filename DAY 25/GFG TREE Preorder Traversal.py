
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Function to return a list containing the preorder traversal of the tree.
def tra(root,x):
    if root is not None:
        x.append(root.data)
        tra(root.left,x)
        tra(root.right,x)
    
def preorder(root):
   
    # code here
    x=[]
    tra(root,x)
    return x
    
    

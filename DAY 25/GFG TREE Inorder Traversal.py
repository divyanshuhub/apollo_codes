

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing the inorder traversal of the tree. 
class Solution:
    
    def InOrder1(self,root,x):
        if root is not None:
            self.InOrder1(root.left,x)
            x.append(root.data)
            self.InOrder1(root.right,x)
        else:
            return
            
    def InOrder(self,root):
        x = []
        self.InOrder1(root,x)
        return x
            

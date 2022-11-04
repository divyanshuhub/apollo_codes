'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
def solu(x,root,level):
    global l
    if not root:
        return
    
    if l<level:
        x.append(root.data)
        l = level
    solu(x,root.left,level+1)
    solu(x,root.right,level+1)
    

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    global l 
    l = 0
    x = []
    solu(x,root,1)
    return x

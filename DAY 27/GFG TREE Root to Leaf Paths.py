
'''
class Node:
    def _init_(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
    
def Paths(root):
    # list to store path
    A=[]
    printPathsRec(root, [], 0,A)
    return A

def printPathsRec(root, path, pathLen,A):
    
    path = path[:pathLen]
    if root is None:
        return
    path.append(root.data)
    pathLen = pathLen + 1
 
    if root.left is None and root.right is None:
        x=path.copy()
        A.append(x)
    else:
        printPathsRec(root.left, path, pathLen,A)
        printPathsRec(root.right, path, pathLen,A)
    
    


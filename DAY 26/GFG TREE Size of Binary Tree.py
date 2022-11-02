def tra(root,x):
    if root:
        x[0]+=1
        tra(root.left,x)
        tra(root.right,x)

def getSize(node):
    # code here
    x = [0]
    tra(node,x)
    return x[0]

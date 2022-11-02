def tra(root,x):
    if root:
        x[0]+=root.data
        tra(root.left,x)
        tra(root.right,x)

def sumBT(root):
    # code here
    x = [0]
    tra(root,x)
    return x[0]

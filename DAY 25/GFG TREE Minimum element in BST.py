def minValue(root):
    ##Your code here
    if root is None:
        return -1
    min = root.data
    while root.left is not None:
        root = root.left
        min = root.data
    return min

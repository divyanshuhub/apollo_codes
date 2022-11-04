
'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        # Code here
        if not root1 and not root2:
            return True
        elif root1 and root2:
            if root1.data==root2.data:
                if self.isIdentical(root1.left, root2.left):
                    if self.isIdentical(root1.right, root2.right):
                        return True
            return False
        else:
            return False

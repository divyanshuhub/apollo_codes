class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        res=[]
        self.X(root,res)
        if(res==sorted(res)):
            return 1
        else:
            return 0
    def X(self,root,res):
        if(root is None):
            return
        self.X(root.left,res)
        res.append(root.data)
        self.X(root.right,res)
        
        
        ####################################################################### way 2 #######################################################
    def tra(self, root, x):
        if not root:
            return
        x.append(root.data)
        self.tra(root.left,x)
        self.tra(root.right,x)
            
    def stvcLeft(self, root):
        x = []
        self.tra(root.left,x)
        for i in x:
            if i>=root.data:
                return False
        return True
        
    def stvcRight(self, root):
        x = []
        self.tra(root.right,x)
        for i in x:
            if i<=root.data:
                return False
        return True
        
        
    def isBST1(self, root):
        #code here
        if root==None:
            return True
        elif root.left is None and root.right is not None:
            #if root.right.data<root.data:
            #    return False
            if not self.stvcRight(root):
                return False
            if self.isBST(root.right):
                return True
            else:
                return False
        elif root.left is not None and root.right is None:
            #if root.left.data>root.data:
            #    return False
            if not self.stvcLeft(root):
                return False
            if self.isBST(root.left):
                return True
            else:
                return False
        elif root.left is None and root.right is None:
            return True
        #elif root.left.data>root.data or root.right.data<root.data:
        elif not self.stvcRight(root) or not self.stvcLeft(root):
            return False
        else:
            if self.isBST(root.left) and self.isBST(root.right):
                return True
            else:
                return False

    

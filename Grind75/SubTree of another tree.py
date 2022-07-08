# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root and not subRoot):
            return True
        if(not root and subRoot):
            return False
        if(not root and not subRoot):
            return True
        
        def sametree(t1,t2):
            if(not t1 and not t2):
                return True
            if(not t1 or not t2):
                return False
            return (t1.val==t2.val) and (sametree(t1.left,t2.left)) and (sametree(t1.right,t2.right))
            
            
        if sametree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
        
        
        
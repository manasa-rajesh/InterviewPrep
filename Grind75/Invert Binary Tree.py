# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def preOrder(node):
            if node==None:
                return
            else:
                preOrder(node.left)
                preOrder(node.right)
                
            node.left,node.right = node.right,node.left
            
        preOrder(root)
        
        return root
        
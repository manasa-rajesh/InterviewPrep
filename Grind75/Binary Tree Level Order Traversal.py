# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = collections.deque()
        queue.append(root)
        while(queue):
            level = []
            for i in range(len(queue)):
                ele = queue.popleft()
                if ele:
                    level.append(ele.val)
                    queue.append(ele.left)
                    queue.append(ele.right)
            if len(level)>0:
                res.append(level)
            
        return res
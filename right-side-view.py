# O(n) time, O(h) space
# DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.helper(root,0,result)
        return result 

    def helper(self, root, level, result):
        if not root:
            return 

        if len(result)==level:
            result.append(root.val)

        self.helper(root.right,level+1,result)
        self.helper(root.left, level+1, result)

# BFS
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None 
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide=node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if rightSide: 
                res.append(rightSide.val)

        return res

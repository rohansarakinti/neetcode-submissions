# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        q = deque()
        q.append(-1)
        q.append(root)
        res = 0
        while q:
            print(q)
            curr = q.popleft()
            if curr == -1:
                if q:
                    res += 1
                    q.append(-1)
                continue
            if curr.left != None:
                q.append(curr.left)
            if curr.right != None:
                q.append(curr.right)
        return res

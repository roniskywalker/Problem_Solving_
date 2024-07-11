# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        final = []
        q = collections.deque()
        q.append(root)
        while q:
            q_len = len(q)
            right_node = None
            for i in range(q_len):
                node = q.popleft()
                if node:
                    right_node = node
                    q.append(node.left)
                    q.append(node.right)
            if right_node:
                final.append(right_node.val)
        return final
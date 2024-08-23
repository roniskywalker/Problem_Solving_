# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(node: Optional[TreeNode], result: List[int]):
            if node is None:
                return
            traverse(node.left, result)
            result.append(node.val)
            traverse(node.right, result)
        result = []
        traverse(root, result)
        return result
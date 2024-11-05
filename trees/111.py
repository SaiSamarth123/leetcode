# 111. Minimum Depth of Binary Tree
# Easy

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        minTreeDepth = 0
        queue = deque()
        queue.append(root)

        while queue:
            minTreeDepth += 1
            levelSize = len(queue)

            for _ in range(levelSize):

                currNode = queue.popleft()

                if not currNode.left and not currNode.right:
                    return minTreeDepth

                if currNode.left:
                    queue.append(currNode.left)

                if currNode.right:
                    queue.append(currNode.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        visited = [None, None]
        lca = self.lowestCommonAncestorUtil(root, p, q, visited)

        if (visited[0] and visited[1]) or (visited[0] and self.find(lca, q)) or (visited[1] and self.find(lca, p)):
            return lca
        
        return None

    def lowestCommonAncestorUtil(self, root: TreeNode, p, q, visited):
        if root == None:
            return None
        if root == p:
            visited[0] = p
            return p
        if root == q:
            visited[0] = q
            return q
        
        lcaL = self.lowestCommonAncestorUtil(root.left, p, q, visited)
        lcaR = self.lowestCommonAncestorUtil(root.right, p, q, visited)

        if lcaL and lcaR:
            return root
        if lcaL:
            return lcaL
        if lcaR:
            return lcaR
        
        return None

    def find(self, root, x):
        if root == None:
            return False
        
        if root == x:
            return True
        
        l = self.find(root.left, x)
        r = self.find(root.right, x)
        return l or r


        



        
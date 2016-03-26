
class Solution(object):
    def searchSubTree(self, node, p, q):
        c = 0
        if node == None:
            return c
        if node == p:
            c += 1
        if node == q:
            c += 1
        if c == 2:
            return 2
        elif node.left != None and node.right != None:
            return c + self.searchSubTree(node.left,p,q) + self.searchSubTree(node.right,p,q)
        elif node.left != None and node.right == None:
            return c + self.searchSubTree(node.left,p,q)
        elif node.left == None and node.right != None:
            return c + self.searchSubTree(node.right,p,q)
        else:
            return c
        
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root == p or root == q:
            return root
        
        c= self.searchSubTree(root.left,p,q)
        if c==1:
            return root
        elif c==2:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return self.lowestCommonAncestor(root.right,p,q)

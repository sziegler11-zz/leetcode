class TreeNode:
     def __init__(self, x=0):
         self.val = x
         self.left = None
         self.right = None

def depth(root):
    if root == None:
        return 0
    else:
        return max(depth(root.left), depth(root.right))+1


def isBalanced(root):
    if root == None:
        return True
    n1=depth(root.left)
    n2=depth(root.right)
    if ((n1-n2) in range(-1,2)) and isBalanced(root.left) and isBalanced(root.right):
        return True
    else:
        return False
        
t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)
t.right.left=TreeNode()
t.right.right=TreeNode()
t.right.right.right=TreeNode()
t.left.left=TreeNode()

print isBalanced(t)

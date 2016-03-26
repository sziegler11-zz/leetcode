class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def genSumList(root):
    if root== None:
        return []
    elif root.left == None and root.right == None:
        return [root.val]
    else:
        a = genSumList(root.left) + genSumList(root.right)
        return [j+root.val for j in a]

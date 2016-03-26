class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


def buildList(root):
        a=[]
        if root == None:
            a.append("bozo")
            return a
        elif root.left == None and root.right == None:
            a.append(root.val)
            return a
        else:
            a.extend(buildList(root.left))
            a.append(root.val)
            a.extend(buildList(root.right))
            return a

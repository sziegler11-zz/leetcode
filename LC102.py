class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def traverse(root):
    a=[]
    #if root.left == None and root.right == None:
       # return [root.val]
    if root == None:
        return a
    else:
        a.append([root.val])
        f=[]
        l=traverse(root.left)
        r=traverse(root.right)
        while len(l) != 0 and len(r) != 0:
            l[0].extend(r[0])
            f.append(l[0])
            l.pop(0)
            r.pop(0)
        if len(l) == 0:
            f.extend(r)
        else:
            f.extend(l)
        
        a.extend(f)
        

    return a
                 
    
    

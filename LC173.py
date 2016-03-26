class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self = root
        
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.right == None:
            return False
        else:
            return True
        

    # @return an integer, the next smallest number
    def next(self):

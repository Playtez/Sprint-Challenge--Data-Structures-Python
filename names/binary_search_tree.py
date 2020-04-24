
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    
    def insert(self, value):
        # self.left and self.right have to be valid nodes
        # for us to call 'insert' on them
        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty
            else:
                #we found a valid parking spot
                self.left = BinarySearchTree(value)
        # other wise, value >= self.value
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        

    # def insert(self,value)
    # pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # search through the tree comparing to the target
        if target == self.value:
            return True
        # if the target is less than self go to left
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
           
        # if target is greater than self go to right
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False

        # continue until target is equal to node 
        # if it is found return True
        # else return False
       

    # Return the maximum value found in the tree
    def get_max(self):
        # if self.right > self.value : move to the right
        if self.right:
            return self.right.get_max()
        else:
        # if self.right does not exist return the value
            return self.value
    

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        #loop though all the node
        cb(self.value)
        # if left exists
        if self.left:
            self.left.for_each(cb)
        #   # call for for each
        #if right exist 
        if self.right:
            self.right.for_each(cb)
        

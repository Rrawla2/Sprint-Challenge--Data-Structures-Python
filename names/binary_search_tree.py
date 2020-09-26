class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            return None
        # RECURSIVE
        if value < self.value:  # if value is less than self.value
            if self.left is None:  # if left child is None
                self.left = BSTNode(value)  # insert here - create new BSTnode
            else:
                self.left.insert(value)  # recursive call

        elif value >= self.value:  # - duplicate values go right
            if self.right is None:  # if right child is None
                self.right = BSTNode(value)  # insert here
            else:
                self.right.insert(value)  # recursive call

    def contains(self, target):
        if self.value is None:
            return None
        if self.value == target:  # check if self.value is target
            return True  # if yes, return True
        # if no,
        elif target < self.value:  # go left
            if self.left:
                return self.left.contains(target)
            else:
                return False
        elif target >= self.value:  # go right
            if self.right:
                return self.right.contains(target)
            else:
                return False
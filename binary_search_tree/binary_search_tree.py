class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value > value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        leftContains = False
        rightContains = False
        if self.value == target:
            return True
        if self.left:
            leftContains = self.left.contains(target)
        if self.right:
            rightContains = self.right.contains(target)

        return leftContains or rightContains

    def get_max(self):
        if self.right:
            max_value = self.right.get_max()
        else:
            return self.value
        return max_value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

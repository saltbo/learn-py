# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        if value >= self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)

        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
        if value == self.value:
            return True

        if value >= self.value and self.right is not None:
            return self.right.contains(value)
        if value < self.value and self.left is not None:
            return self.left.contains(value)

        return False

    def remove(self, value, parent=None):
        if value == self.value:
            # This is the node to be deleted
            if self.left and self.right:
                # Node has two children
                # Find the minimum value in the right subtree
                self.value = self.right.getMinValue()
                # Remove the minimum value from the right subtree
                self.right.remove(self.value, self)

            # Node is left child of parent
            elif parent and parent.left is self:
                parent.left = self.left if self.left else self.right
            # Node is right child of parent
            elif parent and parent.right is self:
                parent.right = self.left if self.left else self.right

            # Node is root node
            else:
                # If the node is the root node and has no children
                if self.left is None and self.right is None:
                    return None
                # If the node is the root node and only has left child
                elif self.left and self.right is None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                # If the node is the root node and only has right child
                elif self.right and self.left is None:
                    self.value = self.right.value
                    self.right = self.right.right
                    self.left = self.right.left

        elif value > self.value and self.right:
            # Node is in the right subtree
            self.right.remove(value, self)
        elif value < self.value and self.left:
            # Node is in the left subtree
            self.left.remove(value, self)

        return self

    def getMinValue(self):
        if self.left:
            return self.left.getMinValue()

        return self.value

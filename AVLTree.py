class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.right_node = None
        self.left_node = None
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    # Check if it is a node or return NULL
    @staticmethod
    def none_value(node):
        if node is None:
            return "NULL"
        else:
            return node.data

    # This operation has a O(1) constant running time complexity
    @staticmethod
    def absolute_value(value):
        int_value = int(value)
        if int_value > 0:
            return int_value
        elif int_value < 0:
            return -int_value
        else:
            return int_value

    @staticmethod
    def left_right_height(node):
        if node.left_node is None:
            left_node_height = -1
        else:
            left_node_height = node.left_node.height
        if node.right_node is None:
            right_node_height = -1
        else:
            right_node_height = node.right_node.height
        return left_node_height, right_node_height

    # This operation has a O(1) constant running time complexity
    @staticmethod
    def max_height(left_height, right_height):
        if left_height < right_height:
            return right_height
        elif left_height > right_height:
            return left_height
        else:
            return left_height

    # This operation has a O(1) constant running time complexity
    def set_height(self, node):
        left_node_height, right_node_height = self.left_right_height(node)
        max_height = self.max_height(left_node_height, right_node_height)
        node.height = max_height + 1

    # NOTE: We only care about the parent nodes while discarding or not taking into account the other half subtree of
    # the parent node.
    # Hence you are only updating the height of the nodes that you pass through or check during the insertion
    # operation backwards.
    # Hence, it also has a O(log N) logarithmic running time complexity.
    def balance_check(self, node):
        self.set_height(node)
        left_node_height, right_node_height = self.left_right_height(node)
        # Checks if it's balanced at that node
        if self.absolute_value(left_node_height - right_node_height) <= 1:
            if node.parent:
                self.balance_check(node.parent)
        else:
            # Unbalanced node
            # Get child node with the highest height
            if left_node_height > right_node_height:
                # Need to rotate right
                # First check if it is doubly left heavy
                left_node = self.doubly_left_heavy(node)
                # if it is not doubly left heavy
                if left_node:
                    # Rotate left
                    self.rotate_left(left_node)
                # Rotate unbalanced node right
                self.rotate_right(node)
            else:
                # Need to rotate left
                # First check if it is doubly right heavy
                right_node = self.doubly_right_heavy(node)
                # if it is not doubly right heavy
                if right_node:
                    self.rotate_right(right_node)
                # Rotate unbalanced node left
                self.rotate_left(node)

    # You want to make sure the left child of the unbalanced node is doubly left heavy
    def doubly_left_heavy(self, node):
        # Get the node's left node
        left_node = node.left_node
        # If the left node right node height is greater than its left node height
        left_height, right_height = self.left_right_height(left_node)
        if right_height > left_height:
            return node.left_node

    # You want to make sure the right child of the unbalanced node is doubly right heavy
    def doubly_right_heavy(self, node):
        # Get node's right node
        right_node = node.right_node
        # If the right node left node height is greater than its right node height
        left_height, right_height = self.left_right_height(right_node)
        if left_height > right_height:
            return node.right_node

    # Right rotation operation
    # This operation has a O(1) constant running time complexity
    def rotate_right(self, node):
        print("rotating to the right on node ", node.data)
        if node.left_node:
            left_node = node.left_node
            if left_node.right_node:
                left_node_right_node = left_node.right_node
                # Set parent for the node's left_node right_node parent
                left_node_right_node.parent = node
            else:
                left_node_right_node = None
            # Set children
            if node.parent:
                parent = node.parent
                # Check if the node is the left or right child of the parent
                if parent.left_node == node:
                    parent.left_node = left_node
                elif parent.right_node == node:
                    parent.right_node = left_node

            left_node.right_node = node
            node.left_node = left_node_right_node

            # Set parents
            if node.parent:
                parent = node.parent
                left_node.parent = parent
            else:
                left_node.parent = None
                self.root = left_node
            node.parent = left_node
            self.set_height(node)
            self.set_height(left_node)

    # Left rotation operation
    # This operation has a O(1) constant running time complexity
    def rotate_left(self, node):
        print("rotating to the left on node ", node.data)
        if node.right_node:
            right_node = node.right_node
            if right_node.left_node:
                right_node_left_node = right_node.left_node
                # Set the node's right_node left_node parent
                right_node_left_node.parent = node
            else:
                right_node_left_node = None
            # Set children
            if node.parent:
                parent = node.parent
                # Check if the node is the left or right child of the parent
                if parent.left_node == node:
                    parent.left_node = right_node
                elif parent.right_node == node:
                    parent.right_node = right_node

            right_node.left_node = node
            node.right_node = right_node_left_node

            # Set parents
            if node.parent:
                parent = node.parent
                right_node.parent = parent
            else:
                right_node.parent = None
                self.root = right_node
            node.parent = right_node
            self.set_height(node)
            self.set_height(right_node)

    # def remove(self, data):
    #     if self.root:
    #         self.remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    # This has a 2*logN running time complexity to be precise
    def insert_node(self, data, node):
        # we have to go on the left subtree
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                new_node = Node(data, node)
                node.left_node = new_node
                # Note this operation is done sequentially to the above operation - it is performed only when
                # the new node is inserted. When the above operation has ended.
                # Hence, the insertion operation has an overall O(log N) logarithmic running time complexity
                self.balance_check(node.left_node)
        # we have to go on the right subtree
        elif data > node.data:
            if node.right_node:
                self.insert_node(data, node.right_node)
            else:
                new_node = Node(data, node)
                node.right_node = new_node
                # Note this operation is done sequentially to the above operation - it is performed only when
                # the new node is inserted. When the above operation has ended.
                # Hence, the insertion operation has an overall O(log N) logarithmic running time complexity
                self.balance_check(node.right_node)

    # Traverse a binary trees
    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    # implementing the in-order traversal for Binary Trees
    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)
        output = "{}, left: {}, right: {}, parent: {}, height: {} ".format(node.data, self.none_value(node.left_node),
                                                                           self.none_value(node.right_node),
                                                                           self.none_value(node.parent), node.height)
        print(output)
        if node.right_node:
            self.traverse_in_order(node.right_node)


if __name__ == "__main__":
    avlTree = AVLTree()
    avlTree.insert(50)
    avlTree.insert(25)
    avlTree.insert(10)
    avlTree.insert(5)
    avlTree.insert(7)
    avlTree.insert(3)
    avlTree.insert(30)
    avlTree.insert(20)
    avlTree.insert(8)
    avlTree.insert(15)
    avlTree.traverse()
    print('------------------------------------------------------------------------------------------------------')

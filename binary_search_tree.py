from node import Node

class BST:
    root = None

    def insert(self, key, value):
        new_node = Node(key, value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            parent = None
            while True:
                parent = current
                if key < current.key:
                    current = current.left_child
                    if current is None:
                        parent.left_child = new_node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = new_node
                        return

    def find_min(self):
        current = self.root
        last = None
        while current is not None:
            last = current
            current = current.left_child
        return last

    def find_max(self):
        current = self.root
        last = None
        while current is not None:
            last = current
            current = current.right_child
        return last

    def remove(self, key):
        current_node = self.root
        parent_node = self.root
        is_left_child = False
        # searching to find the node with the key to delete
        while current_node.key != key:
            parent_node = current_node
            if key < current_node.key:
                is_left_child = True
                current_node = current_node.left_child
            else:
                is_left_child = False
                current_node = current_node.right_child
            if current_node is None:
                return False
        # found node
        node_to_delete = current_node
        # check leaf node
        if node_to_delete.left_child is None \
        and node_to_delete.right_child is None:
            if node_to_delete == self.root:
                self.root = None
            elif is_left_child:
                parent_node.left_child is None
            else:
                parent_node.right_child is None
        # check for 1 child that is on the left
        elif node_to_delete.right_child is None:
            if node_to_delete == self.root:
                self.root = node_to_delete.left_child
            elif is_left_child:
                parent_node.left_child = node_to_delete.left_child
            else:
                parent_node.right_child = node_to_delete.left_child
        # check for 1 child that is on the right
        elif node_to_delete.left_child is None:
            if node_to_delete == self.root:
                self.root == node_to_delete.right_child
            elif is_left_child:
                parent_node.left_child = node_to_delete.right_child
            else:
                parent_node.right_child = node_to_delete.right_child
        # check for 2 children
        else:
            # connect parrent of node to delete to successor
            successor = self.get_successor(node_to_delete)
            if node_to_delete == root:
                root = successor
            elif is_left_child:
                parent_node.left_child = successor
            else:
                parent_node.right_child = successor
            successor.left_child = node_to_delete.left_child
        return True

    def get_successor(self, node_to_delete):
        successor_parent = node_to_delete
        successor = node_to_delete
        # go to the right child
        current = node_to_delete.right_child
        # start going left down the tree until node has no left child
        while current is not None:
            successor_parent = successor
            successor = current
            current = current.left_child
        # if successor is not a right child
        if successor != node_to_delete.right_child:
            successor_parent.left_child = successor.right_child
            successor.right_child = node_to_delete.right_child
        return successor


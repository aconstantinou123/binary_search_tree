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
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if node_to_delete == self.root:
                self.root = None
            elif is_left_child:
                parent_node.left_child = None
            else:
                parent_node.right_child = None
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
            if node_to_delete == self.root:
                self.root = successor
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
    

    def print_self(self):
        current_depth = 0
        parent_node = self.root
        total_depth = self.find_depth(parent_node, 0)
        node_array = [[] for _ in range(total_depth)]
        node_array[0].append(str(self.root.key))
        node_array = self.collect_nodes(parent_node, total_depth, current_depth + 1, node_array)
        for nodes in node_array:
            total_length = 10 * total_depth
            space = int(total_length / (len(nodes) + 1)) * '  '
            nodes[0] = space + nodes[0]
            print(space.join(nodes))

    def find_depth(self, parent, current_depth):
        left_depth = current_depth
        right_depth = current_depth
        if parent is not None:
            current_depth += 1
            left_depth = self.find_depth(parent.left_child, current_depth)
            right_depth = self.find_depth(parent.right_child, current_depth)
        max_depth = left_depth if left_depth > right_depth else right_depth
        return max_depth

    def collect_nodes(self, parent_node, total_depth, current_depth, node_array):
        if current_depth < total_depth:
            empty_node = '--'
            left_node = None if parent_node is None else parent_node.left_child
            right_node = None if parent_node is None else parent_node.right_child
            print_left = empty_node if left_node is None else str(left_node.key)
            print_right = empty_node if right_node is None else str(right_node.key)
            node_array[current_depth].append(print_left)
            node_array[current_depth].append(print_right)
            node_array = self.collect_nodes(left_node, total_depth, current_depth + 1, node_array)
            node_array = self.collect_nodes(right_node, total_depth, current_depth + 1, node_array)
        return node_array 
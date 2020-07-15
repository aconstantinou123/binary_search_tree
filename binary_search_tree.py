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
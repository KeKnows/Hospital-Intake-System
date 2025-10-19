
class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, child_name, side):
        parent_node = self.find(self.root, parent_name)
        if parent_node is None:
            print(f"Parent '{parent_name}' not found.")
            return
        if side not in ["left", "right"]:
            print(f"Invalid side '{side}'. Must be 'left' or 'right'.")
            return
        child_node = DoctorNode(child_name)
        if side == "left":
            if parent_node.left is None:
                parent_node.left = child_node
            else:
                print(f"Left child of '{parent_name}' already exists.")
        else:  # side == "right"
            if parent_node.right is None:
                parent_node.right = child_node
            else:
                print(f"Right child of '{parent_name}' already exists.")

    def find(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        # Search left subtree
        left_result = self.find(node.left, name)
        if left_result:
            return left_result
        # Search right subtree
        return self.find(node.right, name)

    # Traversals
    def preorder(self, node):
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]

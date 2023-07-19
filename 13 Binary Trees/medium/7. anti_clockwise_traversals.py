class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_left_boundary(root):
    if not root:
        return
    if root.left:
        print(root.val, end=" ")
        print_left_boundary(root.left)
    elif root.right:
        print(root.val, end=" ")
        print_left_boundary(root.right)

def print_right_boundary(root):
    if not root:
        return
    if root.right:
        print_right_boundary(root.right)
        print(root.val, end=" ")
    elif root.left:
        print_right_boundary(root.left)
        print(root.val, end=" ")

def print_leaves(root):
    if not root:
        return
    print_leaves(root.left)
    if not root.left and not root.right:
        print(root.val, end=" ")
    print_leaves(root.right)

def boundary_traversal(root):
    if not root:
        return

    print(root.val, end=" ")

    print_left_boundary(root.left)
    print_leaves(root)
    print_right_boundary(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)

print("Anti-Clockwise Boundary Traversal:")
boundary_traversal(root)

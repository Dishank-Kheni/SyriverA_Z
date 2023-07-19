class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left, self.right = left, right

    def createTree(self, list):
        if not list:
            return None
        root = TreeNode(list[0])
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if i < len(list) and list[i]:
                node.left = TreeNode(list[i])
                queue.append(node.left)
            i += 1
            if i < len(list) and list[i]:
                node.right = TreeNode(list[i])
                queue.append(node.right)
            i += 1
        return root

    def height_balanced(self, root):
        # Iterative solution
        if root is None:
            return 0

        stack = [root]
        left_height, right_height = 1, 1
        while stack:
            node = stack.pop()
            if node:
                # max_depth = max(max_depth, depth)
                left_height += 1 if node.left else 0
                stack.append(node.left)
                right_height += 1 if node.right else 0
                stack.append(node.right)
        return True if abs(left_height-right_height) <= 1 else False


if __name__ == "__main__":
    tn = TreeNode(1)
    # root = tn.createTree([3, 9, 20, None, None, 15, 7])
    root = tn.createTree([1, 2, 2, 3, 3, None, None, 4, 4])
    print(tn.height_balanced(root))

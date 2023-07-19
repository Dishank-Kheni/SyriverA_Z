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

    def max_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))

    def diameter_bt(self, root):
        if root is None:
            return 0
        left_height = self.max_depth(root.left)
        right_height = self.max_depth(root.right)
        # left_diameter = self.diameter_bt(root.left)
        # right_diameter = self.diameter_bt(root.right)
        return left_height + right_height


if __name__ == "__main__":
    tn = TreeNode(1)
    # root = tn.createTree([3, 9, 20, None, None, 15, 7])
    # root = tn.createTree([1, 2, 2, 3, 3, None, None, 4, 4])
    # root = tn.createTree([1, 2, 3, 4, 5])
    root = tn.createTree([1, 2])
    print(tn.diameter_bt(root))

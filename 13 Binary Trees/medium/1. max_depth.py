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
        # Iterative solution
        if root is None:
            return 0

        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return max_depth

        # if root is None:
        #     return 0
        # return 1 + max(self.max_depth(root.left), self.max_depth(root.right))


if __name__ == "__main__":
    tn = TreeNode(1)
    root = tn.createTree([3, 9, 20, None, None, 15, 7])
    print(tn.max_depth(root))

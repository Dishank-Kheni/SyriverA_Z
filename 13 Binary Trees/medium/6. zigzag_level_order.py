from collections import deque


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

    # def __repr__(self) -> str:
    def levelorder_traversal(self, root):
        if root is None:
            return []

        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def zigzagTraversal(self, root):
        results = []
        even_level = False
        stack = deque([root])

        while stack:
            n = len(stack)
            level = []
            for _ in range(n):
                if even_level:
                    node = stack.pop()
                    if node.right:
                        stack.appendleft(node.right)
                    if node.left:
                        stack.appendleft(node.left)
                else:
                    node = stack.popleft()
                    if node.left:
                        stack.append(node.left)
                    if node.right:
                        stack.append(node.right)

                level.append(node.val)
            results.append(level)
            even_level = not even_level
        return results


if __name__ == "__main__":
    tn = TreeNode(1)
    root = tn.createTree([3, 9, 20, None, None, 15, 7])
    # root = tn.createTree([1, 2, 2, 3, 3, None, None, 4, 4])
    # root = tn.createTree([1, 2, 3, 4, 5])
    # root = tn.createTree([1, 2])
    print(root.levelorder_traversal(root))
    print(tn.zigzagTraversal(root))

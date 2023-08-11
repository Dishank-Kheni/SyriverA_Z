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

    def preorder_traversal(self, root):
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def preorder_traversal_recursive(self, root, result=[]):
        if root is None:
            return []
        result.append(root.val)
        self.preorder_traversal_recursive(root.left)
        self.preorder_traversal_recursive(root.right)
        return result

    def inorder_traversal(self, root):
        if root is None:
            return []
        stack = []
        result = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
        return result

    def inorder_traversal_recursive(self, root, result=[]):
        if root is None:
            return []

        self.inorder_traversal_recursive(root.left)
        result.append(root.val)
        self.inorder_traversal_recursive(root.right)
        return result

    def postorder_traversal(self, root):
        if root is None:
            return []
        stack = []
        result = []
        while stack or root:
            if root:
                stack.append(root)
                result.insert(0, root.val)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return result

    def postorder_traversal_recursive(self, root, result=[]):
        if root is None:
            return []

        self.postorder_traversal_recursive(root.left)
        self.postorder_traversal_recursive(root.right)
        result.append(root.val)
        return result

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
    # result = []

    temp = []
    result = []
    c = 0

    def rootToKNode(self, root, target, k,   count=0, isrootFound=False):
        if root is None or k == count:
            if count == k:
                self.c += 1
            return self.c

        if root.val == target:
            isrootFound = True

        self.rootToKNode(root.left, k, count +
                         1 if isrootFound else 0, isrootFound)
        self.rootToKNode(root.right, k, count +
                         1 if isrootFound else 0, isrootFound)
        count -= 1
        return self.c


if __name__ == "__main__":
    tn = TreeNode(1)
    # root = tn.createTree([1, 2, 3, 4, 5, 6, 7])
    root = tn.createTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    # root = tn.createTree([1, 2, 3, 4, 5, 6, 7])
    # print(tn.preorder_traversal(root))
    # print(tn.preorder_traversal_recursive(root))
    # print(tn.inorder_traversal_recursive(root))
    # print(tn.inorder_traversal(root))

    # print(tn.postorder_traversal(root))
    # print(tn.postorder_traversal_recursive(root))
    # print(tn.levelorder_traversal(root))
    print(tn.rootToKNode(root, 5, 2, False))

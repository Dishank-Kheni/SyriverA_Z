from collections import defaultdict, deque


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

    column_dict = defaultdict(list)

    def verticle_order_traversal(self, root, row, column):
        if root is None:
            return
        # self.l.append((root.val, row, column))
        if column in self.column_dict:
            self.column_dict[column].append(root.val)
        else:
            self.column_dict[column] = [root.val]

        self.verticle_order_traversal(root.left, row+1, column-1)
        self.verticle_order_traversal(root.right, row+1, column+1)
        self.column_dict = dict(sorted(self.column_dict.items()))
        return [i for i in self.column_dict.values()]
        # return self.column_dict


if __name__ == "__main__":
    tn = TreeNode(1)
    root = tn.createTree([3, 9, 20, None, None, 15, 7])
    print(tn.verticle_order_traversal(root, 0, 0))

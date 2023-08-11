class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root == None or root == p or root == q:
        return root

    # Find p/q in left subtree
    l = lowestCommonAncestor(root.left, p, q)

    # Find p/q in right subtree
    r = lowestCommonAncestor(root.right, p, q)

    # If p and q found in left and right subtree of this node, then this node is LCA
    if l and r:
        return root

    # Else return the node which returned a node from its subtree such that one of its ancestor will be LCA
    return l if l else r


if __name__ == '__main__':

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Given nodes to find LCA
    p = root.left   # Node with value 5
    q = root.left.right.right  # Node with value 4

    # Finding the LCA
    lca_node = lowestCommonAncestor(root, p, q)
    print(lca_node.val)  # 5

def isSameTree(sself, p, q):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False

    stack = [(p, q)]
    while stack:
        p, q = stack.pop()
        if p is None and q is None:
            continue
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        stack.append((p.left, q.left))
        stack.append((p.right, q.right))

    return True

    # else:
    #     return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

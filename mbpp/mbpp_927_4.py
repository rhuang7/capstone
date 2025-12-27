def check(candidate):
    assert (candidate(root)) == 3
    assert (candidate(root1)) == 5 
    assert (candidate(root2)) == 4


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

check(height)
def check(candidate):
    assert candidate(root) == False
    assert candidate(root1) == True
    assert candidate(root2) == False 


def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        left = check_height(node.left)
        right = check_height(node.right)
        if left == -1 or right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    return check_height(root) != -1

check(is_balanced)
class Tree:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def check_binary_tree(root):

    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return check_binary_tree(root.left) and check_binary_tree(root.right)

    return False


root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)

root.left.left = Tree(10)
root.left.right = Tree(30)


if check_binary_tree(root):
    print("Tree is a Binary Tree")
else:
    print("Tree is not a Binary tree")

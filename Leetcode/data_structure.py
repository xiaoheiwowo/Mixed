class Node(object):

    def __init__(self, left, data, right):
        self.left = left
        self.data = data
        self.right = right

    def order(self, tree):
        if tree is not None:
            print(tree.data)
            # return tree.data
            self.order(tree.left)
            self.order(tree.right)


if __name__ == '__main__':

    tree = Node(
        left=Node(
            left=Node(
                left=None,
                data='C',
                right=None),
            data='B',
            right=None),
        data='A',
        right=Node(
            left=None,
            data='D',
            right=None))

    tree.order(tree)
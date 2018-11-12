
ADDED = True

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        self.code = None
        self.weight = 0
        self.is_root = True


def balance_donw_up(root):
    if root == None:
        return
    if root.left!= None:
        if root.weight < root.left.weight:
            root, root.left = root.left, root
    if root.right!= None:
        if root.weight < root.right.weight:
            root, root.left = root.left, root


def balance_left_right(root):
    if root == None:
        return
    if root.left!= None and root.right!= None:
        if root.left.weight > root.right.weight:
            root.left, root.right = root.right, root.left
    balance_left_right(root.left)
    balance_left_right(root.right)


def add_item(root, item):
    if root == None:
        return
    if root.data == item[0]:
        root.weight += 1
        item[0] = ADDED
        return
    #nyt
    if root.is_root and root.weight == 0:
        root.weight = 1
        root.left = Tree()
        root.right = Tree()
        root.right.data = item[0]
        root.right.weight = 1
        root.right.is_root = False
        item[0] = ADDED
        return
    add_item(root.left, item)
    if item[0] == ADDED:
        root.weight = root.weight + 1
        return
    add_item(root.right, item)
    if item[0] == ADDED:
        root.weight = root.weight + 1
        return


def create_tree(root, string):
    for c in string:
        add_item(root, [c])
        #balance_down_up(root)
        balance_left_right(root)

def print_tree(root, level):
    if root == None:
        return
    print(level, root.weight)
    print_tree(root.left, level + 1)
    print_tree(root.right, level + 1)


if __name__ == "__main__":
    string = ""
    with open("input.txt", "r") as f:
        string = f.read().replace(' ', '').replace('\n', '')
    root = Tree()
    create_tree(root, string)
    print_tree(root, 1)
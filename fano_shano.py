
import operator 
import collections
FILENAME = "input.txt"

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        self.code = None

def summ_after_key(symbols, key):
    summ = 0
    summ_flag = False
    for cur_key in symbols.keys():
        if summ_flag:
            summ += symbols[cur_key]
        if cur_key == key:
            summ_flag = True
    return summ


def dict_after_key(symbols, key, right):
    right_flag = False
    for cur_key in symbols.keys():
        if right_flag:
            right[cur_key] = symbols[cur_key]
        if cur_key == key:
            right_flag = True

def find_lr(root):
    left = {}
    right = {}
    summ = 0
    delta = 0
    for key in root.data[0].keys():
        summ += root.data[0][key]
        if summ < summ_after_key(root.data[0], key):
            left[key] = root.data[0][key]
        elif summ > summ_after_key(root.data[0], key):
            if delta > abs(summ - summ_after_key(root.data[0], key)):
                left[key] = root.data[0][key]
                dict_after_key(root.data[0], key, right)
                 #(right = left, left = right)
                return (right, left)
            else:

                if len(left) == 0:
                    right[key] = root.data[0][key]
                    dict_after_key(root.data[0], key, left)
                else:
                    right[key] = root.data[0][key]
                    dict_after_key(root.data[0], key, right)
                return (left, right)
        elif summ == summ_after_key(root.data[0], key):
            left[key] = root.data[0][key]
            dict_after_key(root.data[0], key, right)
            return (left, right)
        delta = abs(summ - summ_after_key(root.data[0], key))



def create_tree(root):
    if len(root.data[0].keys()) == 1:
        return
    nodes = find_lr(root)
    root.left = Tree()
    root.left.data = (nodes[0], sum(nodes[0].values()))
    root.left.code = 1
    root.right = Tree()
    root.right.data =(nodes[1], sum(nodes[1].values()))
    root.right.code = 0
    create_tree(root.left)
    create_tree(root.right)

def root_to_str(root):
    string = ""
    for key in root.data[0].keys():
        string = "{}{}".format(string, key)
    string = "{}{}{}{}".format(string, '(', str(sum(root.data[0].values())), ')')
    return string


def dict_to_str(d):
    string = ""
    for i in d:
        string = "{}{}".format(string, i)
    return string

def sf_code(root, code, sym):
    if len(code)!= 0:
        code.append(root.code)
        return
    if root.left == None and root.right == None:
        if list(root.data[0])[0] == sym:
            code.append(root.code)
        return
    sf_code(root.left, code, sym)
    sf_code(root.right, code, sym)

#call with level = 1
def print_tree(root, level):
    if root == None:
        return
    print(level, root_to_str(root))
    print_tree(root.left, level + 1)
    print_tree(root.right, level + 1)

def fill_symbols(symbols, string):
    for i in range(len(string)):
        if string[i] not in symbols.keys():
            symbols[string[i]] = 1
        else:
            symbols[string[i]] += 1


if __name__ == "__main__":
    symbols = dict()
    string = ""
    with open(FILENAME, "r") as f:
        string = f.read()
    string = string.replace(' ', '').replace('\n', '')
    fill_symbols(symbols, string)
    symbols =  collections.OrderedDict(sorted(symbols.items()))
    symbols = collections.OrderedDict(sorted(symbols.items(), key=operator.itemgetter(1), reverse = True))
    root = Tree()
    root.data = (symbols, sum(symbols.values()))
    create_tree(root)
    print_tree(root,  1)
    code = []
    print("Code:")
    for key in root.data[0].keys():
        sf_code(root, code, key)
        print(key, '(', dict_to_str(code), ')', sep = '', end = ' ')
        code.clear()
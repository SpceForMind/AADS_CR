
import operator 
import collections
FILENAME = "input.txt"

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def summ_after_key(symbols, key):
    summ = 0
    summ_flag = False
    for cur_key in symbols.keys():
        if summ_flag:
            summ += symbols[cur_key]
        if cur_key == key:
            summ_flag = True
    return summ

def find_lr(root):
    left = {}
    stop_key = root.data[0].keys()[0]
    delta = 0
    summ = 0
    for key in root.data[0].keys():
        summ += root.data[0][key]
        if summ < summ_after_key(root.data[0], key):
            left[key] = root.data[0][key]
        if summ < summ_after_key(root.data[0], key):
            left[key] = root.data[0][key]
            right = {}
        elif summ > summ_after_key(root.data[0], key):
            if delta > summ_after_key(root.data[0], key):
                left[key] = root.data[0][key]

        delta = abs(summ - summ_after_key(root.data[0].keys(), key))




def create_tree(root):
    if len(root.data[0]) == 1:
        return


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
    print(root.data)
    print(summ_after_key(root.data[0], 't'))
   # create_tree(root)

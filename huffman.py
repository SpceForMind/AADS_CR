#!/usr/bin/env python3
# Huffman coding algorithm

from collections import OrderedDict
from binarytree import Node
from functools import reduce


def findProbability(text):
    mydict = {}
    text = "".join(text.split())
    for ch in text:
        if ch in mydict:
            mydict[ch] += 1
        else:
            mydict[ch] = 1
    return OrderedDict(sorted(mydict.items(), key=lambda t: (-t[1], t[0]), reverse=0))


def printProbability(prob):
    print("Probabilities:")
    print("\t", end="")
    for key in prob:
        print("{}({})".format(key, prob[key]), end=" ")
    print()


def buildHuffmanCode(prob):
    print()
    list_of_prob = [(key, prob[key]) for key in prob]
    i = 1
    answer = ""
    while(len(list_of_prob) > 1):
        print("Step {}: ".format(i), end="")
        for key, value in list_of_prob:
            print("{}({})".format(key, value), end=" ")
        print()
        new_el = (list_of_prob[-2][0] + list_of_prob[-1][0], list_of_prob[-2][1] + list_of_prob[-1][1])
        if(len(list_of_prob) > 2):
            answer = answer + list_of_prob.pop(len(list_of_prob) - 2)[0] + list_of_prob.pop(len(list_of_prob) - 1)[0] + "|"
        else:
            list_of_prob.pop(len(list_of_prob) - 2)
            list_of_prob.pop(len(list_of_prob) - 1)
        for j in range(0, len(list_of_prob)):
            if list_of_prob[j][1] <= new_el[1]:
                 list_of_prob.insert(j, new_el)
                 break
            if j == len(list_of_prob) - 1:
                list_of_prob.insert(j, new_el)
        i += 1
    print()
    print("Answer: ", end="\n\t")
    print(answer[:-1])
    print()


def printShennonFanoCode(suma, tree, tree_prob, str):

    if len(tree.levels) == 1:
        print("{}: {}".format(tree_prob[tree.value], str))
        suma[0] = suma[0] + len(str)*tree_prob[tree.value][1]

    if tree.left: 
        printShennonFanoCode(suma, tree.left, tree_prob, str + "0")
    if tree.right:
        printShennonFanoCode(suma, tree.right, tree_prob, str + "1")


def buildShennonFanoTree(tree_prob, node, prob):
    if(len(prob) == 1):
        prob = prob[0]
    if isinstance(prob, tuple):
        new_el = prob
    else:
        new_el = (reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]), prob))

    tree_prob.append(new_el)
    node.value = len(tree_prob) - 1

    if isinstance(prob, tuple):
        return

    accum1 = ("", 0)
    accum2 = ("", 0)
    min = 10000
    for i in range(1, len(prob)):
        if(len(prob) == 2):
            if prob[0][1] > prob[1][1]:
                accum1 = prob[1]
                accum2 = prob[0]
            else:
                accum1 = prob[0]
                accum2 = prob[1]
            break
        j = i
        prev_accume1 = accum1
        prev_accume2 = accum2
        accum1 = ("", 0)
        accum2 = ("", 0)
        for el in prob:
            if i != 0:
                accum1 = (accum1[0] + el[0], accum1[1] + el[1])
                i -= 1
            else:
                accum2 = (accum2[0] + el[0], accum2[1] + el[1])
        if min > abs(accum2[1] - accum1[1]):
            min = abs(accum2[1] - accum1[1])
            continue
        else:
            if prev_accume1[1] > prev_accume2[1]:
                accum1 = prob[j-1:]
                accum2 = prob[0:j-1]
            else:
                accum1 = prob[0:j-1]
                accum2 = prob[j-1:]
            break

    
    node.left = Node(0)
    node.right = Node(0)
    buildShennonFanoTree(tree_prob, node.left, accum1)
    buildShennonFanoTree(tree_prob, node.right, accum2)
    return



def buildHuffmanTreeHelp(tree_prob, prob):

    if len(prob) == 1:
        tree_prob.append(prob[0])
        return tree_prob

    el1 = prob[-1]
    el2 = prob[-2]

    prob.pop(len(prob) - 1)
    prob.pop(len(prob) - 1)

    t = el1
    if el1[1] > el2[1]:
        el1 = el2
        el2 = t

    new_el = (el1[0]+el2[0], el1[1]+el2[1])

    tree_prob.append(el1) 
    tree_prob.append(el2)
    prob.insert(0, new_el + (len(tree_prob) - 2, len(tree_prob) - 1))
    prob = sorted(prob, key=lambda x: x[1], reverse=1)

    return buildHuffmanTreeHelp(tree_prob, prob)


def buildHuffmanTree(tree, tree_prob, index):
    
    if(len(tree_prob[index]) == 2):
        return

    tree.left = Node(tree_prob[index][2])
    tree.right = Node(tree_prob[index][3])

    buildHuffmanTree(tree.left, tree_prob, tree_prob[index][2])

    buildHuffmanTree(tree.right, tree_prob, tree_prob[index][3])


def printHuffmanCode(suma, tree, tree_prob, str):

    if len(tree.levels) == 1:
        print("{}: {}".format(tree_prob[tree.value], str))
        suma[0] = suma[0] + len(str)*tree_prob[tree.value][1]

    if tree.left: 
        printHuffmanCode(suma, tree.left, tree_prob, str + "0")
    if tree.right:
        printHuffmanCode(suma, tree.right, tree_prob, str + "1")


def main():
    text = input("Enter your text:\n\t")
    print()
    prob = findProbability(text)
    printProbability(prob)
    buildHuffmanCode(prob)
    print()

    print("------------------------------------------------------Shennon-Fano------------------------------------------------------")
    tree_prob = []
    root = Node(0)
    prob = prob.items()
    buildShennonFanoTree(tree_prob, root, list(prob))

    print(root)
    for counter, value in enumerate(tree_prob):
        print(counter, value)
    print()
    suma = [0]
    printShennonFanoCode(suma, root, tree_prob, "")
    print()
    print("Length of Shennon-Fano coded text: {}".format(suma[0]))
    print("------------------------------------------------------------------------------------------------------------------------")
    print()

    print("---------------------------------------------------------Huffman---------------------------------------------------------")
    tree_prob = []
    prob = sorted(prob, key=lambda t: (t[1], t[0]), reverse=1)
    buildHuffmanTreeHelp(tree_prob, list(prob))
    root = Node(len(tree_prob)-1)
    tree = buildHuffmanTree(root, tree_prob, len(tree_prob)-1)

    print(root)
    for counter, value in enumerate(tree_prob):
        print(counter, value)
    print()
    suma = [0]
    printHuffmanCode(suma, root, tree_prob, "")
    print()
    print("Length of Huffman coded text: {}".format(suma[0]))
    print("------------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
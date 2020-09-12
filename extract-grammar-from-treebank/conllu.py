# -*- coding: utf-8 -*-
class EOS:

    def __init__(self, ls):
        pass

    def show(self):
        print("------------------")


class Node:
    """CoNLL-U formatting taken from:
    https://universaldependencies.org/docs/format.html
    """
    
    def __init__(self, ls):

        self.ID = ls[0]
        self.FORM = ls[1]
        self.LEMMA = ls[2]
        self.UPOSTAG = ls[3]
        self.XPOSTAG = ls[4]
        self.FEATS = ls[5]
        self.HEAD = ls[6]
        self.DEPREL = ls[7]
        self.DEPS = ls[8]
        self.MISC = ls[9]

        self.children = []

    def addChild(self, childNode):

        rel = childNode.DEPREL
        self.children.append((rel, childNode))

    def toString(self):
        return '({} {})'.format(self.FORM, self.HEAD)

    def show(self):
        print('{} {}'.format(self.FORM, self.HEAD))


class DepTree:

    def __init__(self, sentence):

        self.sentence = sentence
        # root node of a dependency tree
        self.root = self.getRoot()
        # dependency tree as an adjacency dictionary
        self.adjDict = {}
        self.mkDepTree()

    def getRoot(self):

        root = "-1"
        for node in self.sentence:
            if node.HEAD == "0":
                root = node
                break

        if root != "-1":
            return root
        else:
            emptyNode = Node(["" for i in range(10)])
            return emptyNode

    def mkDepTree(self):

        for node in self.sentence:

            for maybeChild in self.sentence:

                if maybeChild.HEAD == node.ID:
                    node.addChild(maybeChild)

            self.adjDict[node.ID] = node
            
    def show(self):

        # show tree, while checking that a cycle
        # didn't sneak in (cycle: node's child is its
        # own parent)

        class CycleError:
            pass

        for id in self.adjDict:
            n = self.adjDict[id]

            chIds = []
            for rel, chld in n.children:
                chIds.append(chld.ID)

            print("{} {} {}".format(id, n.FORM, chIds))

        # visited nodes array
        shown = []

        cur = self.adjDict[self.root.ID]
        # stack
        toShow = [cur]

        # while stack is not empty
        while (toShow != []) or (toShow == ["|"]):

            # pop stack
            top = len(toShow) - 1
            cur = toShow[top]
            toShow.pop(top)

            if cur == "|":
                print(" ) ", end="")
                continue
            elif cur not in shown:
                print(" ( {} {} {}".format(cur.FORM, cur.ID, cur.HEAD ), end="")
                shown.append(cur)
            else:
                raise CycleError("Cycle present in tree") 

            toShow.append("|")
            for rel, child in cur.children:
                toShow.append(child)

        print()
        print("------------------------")

# -*- coding: utf-8 -*-

from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
from conllu import *
import argparse


GRAMMAR_STR = """
S -> NP VP
VP -> "saw" | "ate"
NP -> "cat"
"""

grammar = CFG.fromstring(GRAMMAR_STR)

# CoNLL format: 1   पार्टी  पार्टी  n   NNP cat-n|gen-f|num-sg|pers-3|case-d|vib-0|tam-0|chunkId-NP|stype-|voicetype-   3   nmod    _   _


def getCol(matrix, n):
    """Get n'th column of matrix"""

    def selective(ls):
        if (len(ls) == 10):
            return ls[n]
        else:
            return "EOS"

    col = map(selective, matrix)
    return list(col)


def mkArgparse():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", 
                        type=str,
                        help="source file to read from")
    return parser 


if __name__ == "__main__":

    parser = mkArgparse()
    args = parser.parse_args()

    s = []
    with open(args.file, "r+") as f:
        s = f.read()
        s = s.split("\n")
    
    for i, row in enumerate(s):
        s[i] = row.split("\t")

    conlluTrees = []
    sentence = []
    for row in s:
        if len(row) == 10:
            conllu_obj = Node(row)
            sentence.append(conllu_obj)
        else:
            if sentence != []:
                conllu_obj = EOS(row)
                conlluTrees.append(DepTree(sentence))
                sentence = []

    for tree in conlluTrees:
        tree.show()

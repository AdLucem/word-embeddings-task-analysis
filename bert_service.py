# on another CPU machine
from bert_serving.client import BertClient

IP = '10.4.16.161'
SENTENCES = "sentences.txt"


def cosine(v1, v2):
    c = 0
    rvector = v1
    for i in range(len(rvector)):
        c += v1[i] * v2[i]

    cosine = c / float((sum(v1) * sum(v2)) ** 0.5)
    return cosine


with open(SENTENCES, 'r+') as f:
    sentences = f.readlines()

bc = BertClient(ip='10.4.16.161')  # ip address of the GPU machine

n = len(sentences)
for i in range(0, n, 3):
    s1 = sentences[i]
    s2 = sentences[i + 1]
    enc = bc.encode([s1, s2])

    l1 = enc[0]
    l2 = enc[1]
    rvector = l1
    sim = cosine(l1, l2)
    print(s1)
    print(s2)
    print("similarity: ", sim)
    print("--------------------------------------")


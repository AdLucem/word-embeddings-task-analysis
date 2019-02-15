"""Input: ./data_module/corpus.txt, where the corpus is a text file where each line is a string of whitespace-separated words with all punctuation marks stripped out"""


def tokenize(sentence):
    """Tokenizes the sentence. Currently does so
    only by whitespace"""
    return sentence.split(" ")


def get_sentences(filename):
    """Fetch the sentences as a tokenized list-of-lists from
    the file"""

    with open(filename, "r+") as f:
        s = f.readlines()

        tokens_s = []
        for sentence in s:
            tok_s = tokenize(sentence)
            tokens_s.append(tok_s)

        return tokens_s



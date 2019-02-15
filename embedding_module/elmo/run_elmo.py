from allennlp.modules.elmo import batch_to_ids
from allennlp.commands.elmo import ElmoEmbedder
import json


options_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_options.json"
weight_file = "https://s3-us-west-2.amazonaws.com/allennlp/models/elmo/2x4096_512_2048cnn_2xhighway/elmo_2x4096_512_2048cnn_2xhighway_weights.hdf5"

def initialize():

    elmo = ElmoEmbedder()
    return elmo

def run_elmo(sentences):
    embeddings = elmo.batch_to_embeddings(sentences)

    # taking only the first element of embeddings tensor
    representations = embeddings[0]

    outLs = []

    # iterating through each "sentence" of embeddings
    for i in range(len(representations)):
        s = representations[i]

        # iterating though each layer of embeddings for a sentence
        for layer in list(s):

            # for "word" - sequence unit - in layer
            for j in range(len(layer)):

                if j >= len(sentences[i]):
                    outLs.append("Empty")
                else:
                    outLs.append(sentences[i][j])

                outLs.append(str(tensorToList(layer[j])))

            # adding a layerwise delimiter
            outLs.append("----")

        # adding a sentence-wise delimiter
        outLs.append("====")

    return outLs


#print("Length of tensor list:",len(embeddings))
#print("Num. of sentences:", len(embeddings[0]))
#print("Number of layers:", len(embeddings[0][0]))
#print("Max. sentence length:", len(embeddings[0][0][0]))
#print("Each word vector:", len(embeddings[0][0][0][0]))

# embeddings['elmo_representations'] is length two list of tensors.
# Each element contains one layer of ELMo representations with shape
# (2, 3, 1024).
#   2    - the batch size
#   3    - the sequence length of the batch
#   1024 - the length of each ELMo vector


#!/bin/bash

# install allennlp
pip install --user allennlp

# install chainer, which for some reason
# is a required module that context2vec
# does not install
pip install --user chainer

# install cupy too, for the same reasons
pip install --user cupy

# install nltk for the corpuses
pip install --user nltk

# install plotly for the graphs
pip install --user plotly

# install context2vec
cd $HOME
git clone https://github.com/orenmel/context2vec.git
cd context2vec
python setup.py install


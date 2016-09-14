import os
import json
from nltk.corpus import PlaintextCorpusReader
from nltk import bigrams
from nltk import ConditionalFreqDist

wordlist = []
corpusroot = os.path.abspath('corpus')
poetcorpus = PlaintextCorpusReader(corpusroot, '.*')

invocab = open('syllvocab')
syllvocab = json.load(invocab)
invocab.close()
vocab = {}

for syllnum in syllvocab:
    for word in syllnum:
        vocab[word] = 1

for file in poetcorpus.fileids():
    print file

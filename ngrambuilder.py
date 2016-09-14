import os
import json
from nltk.corpus import PlaintextCorpusReader
from nltk import bigrams
from nltk import ConditionalFreqDist

""" Creates a conditional frequency distribution from a corpus of texts
"""
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
    filewords = list(poetcorpus.words(fileids = file))
    for word in filewords:
        wordlist.append(word.lower())

# should remove page numbers and stuff

for word in wordlist:
    if not vocab.has_key(word):
        wordlist.remove(word)

corpbigrams = bigrams(wordlist)
cfd = ConditionalFreqDist(corpbigrams)
# deleting words changes relations. Doesn't account for separation between poems

with open('cfd', 'w') as out:
    json.dump(cfd, out)

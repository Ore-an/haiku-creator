#!usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
import os
import json
from nltk.corpus import PlaintextCorpusReader
from nltk import word_tokenize
from collections import defaultdict
import itertools
from math import log
from haikuconf import *
from haikuutils import *

""" Creates an ngram language model from a corpus of texts
"""

#Load corpus
corpusroot = os.path.abspath('corpus')
corpus = PlaintextCorpusReader(corpusroot, '.*')

w2i = load_dict('w2i')

def count_trigrams(inputdata):

    '''Extracts all the trigrams from a a file, returns a dictionary of the counts.'''

    tri_counts = defaultdict(int)
    for j in range(len(inputdata)-(2)): # the last two words can't form a trigram
        trigram = inputdata[j:j+3] # the slice is a trigram
        tri_counts[tuple(trigram)] += 1

    return tri_counts

def trigram_smooth(counts):
    '''Does alpha smoothing so as to accommodate for unseen trigrams. Accepts a dictionary of counts.'''

    for trigram in itertools.product(w2i.values(), repeat=3):
        counts[tuple(trigram)] += ALPHA

def group_trig(trig_dict):
    '''Groups a dictionary of trigrams by first and second word'''
    grouped_trig = {}
    for i, j in itertools.groupby(sorted(trig_dict), key=lambda x: x[0]):
        for k, l in itertools.groupby(j, key= lambda x: x[1]):
            grouped_trig[(i,k)] = list(l)

    return grouped_trig

def trigram_prob(tri_counts):
    '''Calculates probabilities for the trigrams by grouping them by condition'''
    tri_prob = defaultdict(dict)
    grouped_trig = group_trig(tri_counts)

    # sums all the counts for condition and then calculates probabilities
    for i in grouped_trig.keys():
        tri_tot_count = sum([tri_counts[j] for j in grouped_trig[i]])

        # TODO: Change the grouping and counting hack to something better

        for j in grouped_trig[i]:
            tri_prob[i][j[2]] = log(tri_counts[j]) - log(tri_tot_count)


    return tri_prob


wordlist = []
for file in corpus.fileids():
    filewords = list(corpus.words(fileids = file))
    wordlist.extend([w2i.get(w.lower()) for w in filewords if w2i.get(w.lower()) is not None])

tri_counts = count_trigrams(wordlist)
if SMOOTH > 0:
    trigram_smooth(tri_counts)
tri_prob = trigram_prob(tri_counts)

print(tri_prob.items()[0:3])

save_dict('triprob', tri_prob)



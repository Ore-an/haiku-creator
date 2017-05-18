#!usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
import nltk
import json
from haikuconf import *
from haikuutils import *


def syllcount(pron): # counts syllables in a pronunciation
    syllnum = 0
    for i in pron:
        if i.isalpha() == False: #cmudict has numbers for stress associated with the nucleus of the syllable
            syllnum += 1
    return syllnum

def build_vocabs(data):# data must be a tuple of (entry, pronounciation) in CMU dictionary style

    w2i = STARTVOCAB # word to index dictionary
    startlen = len(STARTVOCAB)
    wordsyll = [[] for i in range(MAXSYLL)]

    for index, entry in enumerate(data):
        w2i[entry[0]] = index + startlen
        syll = syllcount(entry[1])
        if syll > 0:
            wordsyll[syll - 1].append(index + startlen)

    i2w = {v:k for k,v in w2i.items()}

    return w2i, i2w, wordsyll



w2i, i2w, syllvocab = build_vocabs(nltk.corpus.cmudict.entries())

save_dict('w2i', w2i)
save_dict('i2w', i2w)
save_dict('syllvocab', syllvocab)

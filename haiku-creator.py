#!usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
import random
import json
from haikuconf import *
from haikuutils import *

verses = [[] for i in range(len(HAIKUSYLL))]

invocab = open('syllvocab')
syllvocab = json.load(invocab)
invocab.close()


def word_search(syllnum, wordhistory):

    """Returns a word with syllnum syllables or, if there's no single word
       of that lenght, 2+ words that fill that lenght

"""

    syllnum -= 1 # readjusting for zero-indexing
    
    if syllvocab[syllnum]:
        return random.choice(syllvocab[syllnum])
    else:
        rand = random.randint(1, (syllnum -1))
        leftwords = wordsearch(syllnum - rand, wordhistory)
        rightwords = wordsearch(rand, wordhistory)
        return (leftwords + ' ' + rightwords)
    
def compose_haiku(haikusyll):

    for i in range(len(verses)):
        versesyll = haikusyll[i]
        wordssyll = []
        wordsnum = random.randint(1, versesyll) # words to fit in verse
        usedsyll = 0
        
        for j in range(1, (wordsnum + 1)):
            # keep at least 1 syllable for remaining words
            maxsyll = versesyll - (usedsyll + (wordsnum - j)) # divide verse in words of various lenghts
            wsyll = random.randint(1, maxsyll)
            wordssyll.append(wsyll)
            usedsyll += wsyll
            
        if usedsyll != versesyll:
            # fills verse if open syllables remain
            wordssyll.append(versesyll - usedsyll)

        random.shuffle(wordssyll)
        print (wordssyll)
        
        for wl in wordssyll:
            word = word_search(wl, )
            verses[i].append(word)

        verses[i] = ' '.join(verses[i])
        verses[i].capitalize()
        print(verses[i])

compose_haiku(HAIKUSYLL)



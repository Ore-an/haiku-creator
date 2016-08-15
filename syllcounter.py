import nltk
import json

MAXSYLL = 14

entries = nltk.corpus.cmudict.entries()
syllvocab = [[] for i in range(MAXSYLL)]

def syllcount(pron):
    syllnum = 0
    for i in pron:
        if i.isalpha() == False:
            syllnum += 1
    return syllnum

for entry, pron in entries:
    syll = syllcount(pron)
    if syll > 0:
        syllvocab[syll - 1].append(entry)

with open('syllvocab', 'w') as out:
    json.dump(syllvocab, out)

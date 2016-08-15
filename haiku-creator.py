import random
import json

HAIKUSYLL = [5, 7, 5]
verses = [[] for i in range(len(HAIKUSYLL))]

invocab = open('syllvocab')
syllvocab = json.load(invocab)
invocab.close()

def word_search(syllnum: int) -> str:
    """Returns a word with syllnum syllables or, if there's no single word
       of that lenght, 2+ words that fill that lenght
"""

    syllnum -= 1 # readjusting for index
    
    if syllvocab[syllnum]:
        return random.choice(syllvocab[syllnum])
    else:
        rand = random.randint(1, (syllnum -1))
        return (wordsearch(syllnum - rand) + ' ' + wordsearch(rand))
    
def compose_haiku(haikusyll: list) -> str:

    for i in range(len(verses)):
        versesyll = haikusyll[i]
        wordssyll = []
        wordsnum = random.randint(1, versesyll) # words to fit in verse
        usedsyll = 0
        
        for j in range(1, (wordsnum + 1)):
            # keep at least 1 syllable for remaining words
            maxwsyll = versesyll - (usedsyll + (wordsnum - j))
            # divide verse in words of various lenghts
            wsyll = random.randint(1, maxwsyll)
            wordssyll.append(wsyll)
            usedsyll += wsyll
            # TODO code that can't leave holes
            
        if usedsyll != versesyll:
            # fills verse 
            wordssyll.append(versesyll - usedsyll)

        random.shuffle(wordssyll)
        print (wordssyll)
        
        for wl in wordssyll:
            word = word_search(wl)
            verses[i].append(word)

        verses[i] = ' '.join(verses[i])
        verses[i].capitalize()
        print(verses[i])

compose_haiku(HAIKUSYLL)


"""TODO take corpus annotated for syntactical categories and build the haikus
   respecting syntax OR use Markov chains to make better haikus
"""

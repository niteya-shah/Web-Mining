from nltk.corpus import wordnet
from autocorrect import spell
import numpy as np

def syn(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return set(synonyms)

def tokenise(sent):
    return list(set(sent.split()))

def clean(word):
    return spell(word)

def val(docs):
    wordlist=set()
    for word in tokenise(docs.lower()):
        word=clean(word)
        wordlist=wordlist.union(syn(word))
    return list(wordlist)

def cossim(d1,d2):
    return np.sum(np.array(d1)*np.array(d2))/(np.linalg.norm(d1)*np.linalg.norm(d2))

def wlist(doc,corpus):
    wordlist=[0]*len(corpus)
    for i in val(doc):
        try:
            wordlist[corpus.index(i)]+=1
        except Exception as e:
            pass
    return wordlist

query="shiny metal with higher conductivity"

doc1="Gold is a chemical element with symbol Au (from Latin: aurum) and atomic number 79, making it one of the higher atomic number elements that occur naturally. In its purest form, it is a bright, slightly reddish yellow, dense, soft, malleable, and ductile metal. Chemically, gold is a transition metal and a group 11 element. It is one of the least reactive chemical elements and is solid under standard conditions. Gold often occurs in free elemental (native) form, as nuggets or grains, in rocks, in veins, and in alluvial deposits. It occurs in a solid solution series with the native element silver (as electrum) and also naturally alloyed with copper and palladium. Less commonly, it occurs in minerals as gold compounds, often with tellurium (gold tellurides)"
doc2="Silver is a chemical element with symbol Ag (from the Latin argentum, derived from the Proto-Indo-European h₂erǵ: 'shiny' or 'white') and atomic number 47. A soft, white, lustrous transition metal, it exhibits the highest electrical conductivity, thermal conductivity, and reflectivity of any metal. The metal is found in the Earth's crust in the pure, free elemental form ('native silver'), as an alloy with gold and other metals, and in minerals such as argentite and chlorargyrite. Most silver is produced as a byproduct of copper, gold, lead, and zinc refining."

docs=doc1+doc2

wordcorp=val(docs)
d1list=wlist(doc1,wordcorp)
d2list=wlist(doc2,wordcorp)
querylist=wlist(query,wordcorp)
c1=cossim(d1list,querylist)
c2=cossim(d2list,querylist)
print("similarity of doc 1 ",c1)
print("similarity of doc 2 ",c2)
if(c1>c2):
    print("Document 1 is more similar to query")
else:
    print("Document 2 is more similar to query")

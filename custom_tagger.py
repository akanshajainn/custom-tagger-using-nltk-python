#One solution is to create a manual UnigramTagger that backs off to the NLTK tagger. Something like this:

#importing dependencies
import nltk.tag, nltk.data
#path to the already existing tagger: nltk_data/taggers/maxent_treebank_pos_tagger/english.pickle
#Find it by searching in your computer where you downloaded the nltk package.
#If not found then download by running 'nltk.download()' and you will get a pop up window, download all.
path='PUT YOUR PATH HERE'
default_tagger = nltk.data.load(path)
model = {'select': 'VB', 'important': 'JJ'} #add your custom tags
tagger = nltk.tag.UnigramTagger(model=model, backoff=default_tagger)
#Input to test
tagger.tag(['select', 'the', 'important', 'files'])
#Then you get
#[('select', 'VB'), ('the', 'DT'), ('important', 'JJ'), ('files', 'NNS')]

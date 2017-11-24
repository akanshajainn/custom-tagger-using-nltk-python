#One solution is to create a manual UnigramTagger that backs off to the NLTK tagger. Something like this:

import nltk.tag, nltk.data
path='/Users/akanshajain/nltk_data/taggers/maxent_treebank_pos_tagger/english.pickle'
default_tagger = nltk.data.load(path)
model = {'select': 'VB'} #add your custom tags
tagger = nltk.tag.UnigramTagger(model=model, backoff=default_tagger)
#Then you get
tagger.tag(['select', 'the', 'files'])
#[('select', 'VB'), ('the', 'DT'), ('files', 'NNS')]

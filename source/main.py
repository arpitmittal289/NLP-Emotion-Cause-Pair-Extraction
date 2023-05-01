import pandas as pd
import numpy as np
import nltk
import random
import re
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.optim.lr_scheduler import StepLR, MultiStepLR
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models.keyedvectors import KeyedVectors
import numpy as np
from torch.utils.data.sampler import SubsetRandomSampler
from torch.nn.utils.rnn import pad_sequence, pack_padded_sequence, pad_packed_sequence
import json
import benepar   
import nltk
import re
from pycorenlp import *
import spacy
import pickle

nlp = spacy.load('en_core_web_sm')

def find_root_of_sentence(doc):
    root_token = None
    for token in doc:
        if (token.dep_ == "ROOT"):
            root_token = token
    return root_token

def find_other_verbs(doc, root_token):
    other_verbs = []
    for token in doc:
        ancestors = list(token.ancestors)
        if (token.pos_ == "VERB" and len(ancestors) == 1\
            and ancestors[0] == root_token):
            other_verbs.append(token)
    return other_verbs

def get_clause_token_span_for_verb(verb, doc, all_verbs):
    first_token_index = len(doc)
    last_token_index = 0
    this_verb_children = list(verb.children)
    for child in this_verb_children:
        if (child not in all_verbs):
            if (child.i < first_token_index):
                first_token_index = child.i
            if (child.i > last_token_index):
                last_token_index = child.i
    return(first_token_index, last_token_index)

df_train = pd.read_csv("Electronics_split1.csv", names=["Ratings", "Reviews"], nrows=100)
reviews = df_train['Reviews']
review_sent = df_train.apply(lambda row: nltk.sent_tokenize(row['Reviews']), axis=1)

review_ds = []

for r in range(len(review_sent)):
    temp = []
    for s in range(len(review_sent[r])):
        doc = nlp(review_sent[r][s])
        root_token = find_root_of_sentence(doc)
        other_verbs = find_other_verbs(doc, root_token)

        token_spans = []   
        all_verbs = [root_token] + other_verbs
        for other_verb in all_verbs:
            (first_token_index, last_token_index) = \
            get_clause_token_span_for_verb(other_verb, doc, all_verbs)
            token_spans.append((first_token_index, last_token_index))

        sentence_clauses = []
        for token_span in token_spans:
            start = token_span[0]
            end = token_span[1]
            if (start < end):
                clause = doc[start:end]
                sentence_clauses.append(clause)

        sentence_clauses = sorted(sentence_clauses, key=lambda tup: tup[0])
        clauses_text = [clause.text for clause in sentence_clauses]

        temp.append(clauses_text)
    review_ds.append(temp)

with open("review_ds.txt", "wb") as fp:   #Pickling
  pickle.dump(review_ds, fp)

with open("review_ds.txt", "rb") as fp:   # Unpickling
  b = pickle.load(fp)



token_spans = []   
all_verbs = [root_token] + other_verbs
for other_verb in all_verbs:
    (first_token_index, last_token_index) = \
     get_clause_token_span_for_verb(other_verb, 
                                    doc, all_verbs)
    token_spans.append((first_token_index, 
                        last_token_index))



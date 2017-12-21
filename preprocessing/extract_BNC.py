from nltk.corpus.reader.bnc import BNCCorpusReader
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from collections import Counter
import os
import csv

# контроль по списку
# кластеризовать слова w2v - матричные и зависимые


stopw = set(stopwords.words('english'))
with open('control_verbs.txt','r',encoding='utf-8') as f:
    control = {x.strip() for x in f.readlines()}
lmzr = WordNetLemmatizer()

r = BNCCorpusReader(root='../corpus/BNC/',fileids=r'B/\w*/\w*\.xml')
tagged_sents = r.tagged_sents(c5=True)
sents = r.sents()
matrix = []
data = []
for tsent,sent in zip(tagged_sents[:50000],sents[:50000]):
    for i in range(1,len(tsent)):
        existence = tsent[i][1] is not None and tsent[i-1][1] is not None
        now_bareinf = existence and tsent[i][1][0] == 'V' and tsent[i][1][2] == 'I'
        now_inf = existence and tsent[i][1] == 'TO0'
        now_ger = existence and tsent[i][1][0] == 'V' and tsent[i][1][2] == 'G'
        prev_matrix = existence and tsent[i-1][1].startswith('VV')
        prev_lex = existence and tsent[i-1][0].lower() not in stopw
        if prev_matrix and prev_lex:
            if now_ger:
                data.append((' '.join(sent),[str(x) for x in tsent],
                             ' '.join(sent[i-1:i+1]),sent[i-1],lmzr.lemmatize(sent[i-1].lower(),'v'),
                             sent[i],lmzr.lemmatize(sent[i].lower(),'v'),
                             int(lmzr.lemmatize(sent[i-1].lower(),'v') in control),'gerund'))
            elif now_inf:
                data.append((' '.join(sent),[str(x) for x in tsent],
                             ' '.join(sent[i-1:i+2]),sent[i-1],lmzr.lemmatize(sent[i-1].lower(),'v'),
                             sent[i+1],lmzr.lemmatize(sent[i+1].lower(),'v'),
                             int(lmzr.lemmatize(sent[i-1].lower(),'v') in control), 'inf'))
            elif now_bareinf:
                data.append((' '.join(sent),[str(x) for x in tsent],
                             ' '.join(sent[i-1:i+1]),sent[i-1],lmzr.lemmatize(sent[i-1].lower(),'v'),
                             sent[i],lmzr.lemmatize(sent[i].lower(),'v'),
                             int(lmzr.lemmatize(sent[i-1].lower(),'v') in control),'bareinf'))

with open('data.csv','w',encoding='utf-8-sig',newline='') as f:
    csvw = csv.writer(f,delimiter=';',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csvw.writerow(['sent','tagged sent','construction','matrix','matrix_lemma',
                   'embedded','embedded_lemma','control?','answer'])
    for d in data:
        csvw.writerow(d)

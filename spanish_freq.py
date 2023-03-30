import os
import re

ROOT = './corpus/'
files = os.listdir(ROOT)
import spacy
nlp = spacy.load('es_core_news_md')

for f in files:
    if f.startswith('spanish'):
        file = open(ROOT+f,'r',encoding = 'latin-1').read()
        docs = file.split('<doc id=')[1:]
        for item in docs:
            start = item.find('>')  
            text = item[start+1:].split('</doc>')[0]
            text = text.replace('\n',' ')
            text = re.sub(' +',' ',text).strip(' ')
            text_ = nlp(text)
        print(XXX)
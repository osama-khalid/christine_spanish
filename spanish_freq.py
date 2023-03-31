import os
import re
import tqdm

ROOT = './corpus/'
files = os.listdir(ROOT)
bigram_count = {}
unigram_count = {}
for f in tqdm.tqdm(files):
    if f.startswith('spanish'):
        file = open(ROOT+f,'r',encoding = 'latin-1').read()
        docs = file.split('<doc id=')[1:]
        for item in docs:
            start = item.find('>')  
            text = item[start+1:].split('</doc>')[0]
            text = text.replace('\n',' ')
            text = re.sub(r'[^\w\s]', ' ',text).lower()

            text = [re.sub(' +',' ',text).strip(' ')]
            unigrams = text[0].split(' ')            
            bigrams = ['_'.join(b) for l in text for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
            uni = list(set(unigrams))
            for u in uni:
                if u not in unigram_count:
                    unigram_count[u]=0
                unigram_count[u] += unigrams.count(u)
                
                
            bi = list(set(bigrams))
            for u in bi:
                if u not in bigram_count:
                    bigram_count[u]=0
                bigram_count[u] += bigrams.count(u)                
                
                
import csv

with open('unigram_freq.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')
    for u in unigram_count:
        employee_writer.writerow([u,unigram_count[u]])
        

with open('biigram_freq.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')
    for u in unigram_count:
        employee_writer.writerow([u.replace('_',' '),bigram_count[u]])        
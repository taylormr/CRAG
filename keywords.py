from import_csv import *
from rake_nltk import Rake
import csv

import operator
df = load_csv()
f= open("SmartStoplist.txt")
stoplist = f.read()
rake_object = Rake(stopwords =stoplist, min_length = 1, max_length = 2)
f.close()

keywords= []
for index, x in df.iterrows():
    if type(x[4]) != float:
        
        rake_object.extract_keywords_from_text(x[4])
        key = rake_object.get_ranked_phrases()
    elif type(x[2]) != float:
        rake_object.extract_keywords_from_text(x[2])
        key = rake_object.get_ranked_phrases()
    else: 
        key = []

    keywords.append(key)
    
with open("keywords.csv","w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(keywords)    

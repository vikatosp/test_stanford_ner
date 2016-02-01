import os
from nltk.tag.stanford import StanfordNERTagger
# java_path = "C:/Program Files/Java/jdk1.8.0_05/bin/java.exe"
# os.environ['JAVAHOME'] = java_path

# path2 = 'C:/Users/Pantelis/Desktop/stanford-ner'
st =  StanfordNERTagger('classifiers/english.all.3class.distsim.crf.ser.gz', 'stanford-ner.jar')

f1 = open('Dostoyevski_TheGambler.txt','r')
f2 = open('Dostoyevsky_TheGambler_Results.txt','w')
f3 = open('Dostoyevsky_TheGambler_PERSONS.txt','w')
f4 = open('Dostoyevsky_TheGambler_Unique_PERSONS.txt','w')

book=f1.read()
persons =[]
#print book
results2= st.tag(book.split())

for name,entity in results2:
    print name +" " + entity
    f2.write(name +" " + entity+"\n" )
    if entity == "PERSON":
        f3.write(name +"\n")
        if name not in persons:
            persons.append(name)
for k in persons:
    f4.write(k+"\n")

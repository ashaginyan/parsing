import spacy
from spacy.lang.ru.examples import sentences

# https://github.com/tecoholic/ner-annotator.git

# nlp = spacy.blank('ru')
nlp = spacy.load("ru_core_news_sm")

f = open('telegram.txt', 'r')
text = f.read()
f.close()

doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)
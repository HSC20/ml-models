import en_core_web_sm
nlp = en_core_web_sm.load()
doc = nlp('I am Sanjay my country is India i am 22 year old ,i am work in Google as a engineer')
print([(X.text, X.label_) for X in doc.ents])

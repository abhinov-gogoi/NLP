# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_lg")

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week. ")

text2 = """
Hello Mike my name is John Doe. I need to submit an insurance claim for my mother Mary Johnson.
She is a White Christian American and lives in the U.S.A. My Father is Indian
My Wife is a Buddhist and also Chinese.
My Credit Card cvv number is two four three. And email is mike at gmail dot com"""

doc = nlp(text2)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

print("\n\n----------------------- SENTENCES ----------------------------------------")

for sentences in doc.sents:
    print(sentences)

print("---------------------------------------------------------------")

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, f'-----------[{entity.label_}]')

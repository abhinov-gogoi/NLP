# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("/home/abhinov/PycharmProjects/NLP/model-best")

# Process whole documents
text2 = """
Mike my name is John Doe. I need to submit an insurance claim for my mother Mary Johnson.
She is a American and lives in the U.S.A. My Father is Indian
My Wife is a Buddhist and also Chinese. Obama is African American.
My cvv number is two four three. And email is mike at gmail dot com. 
The Hispanic population in the United States is growing rapidly.
Barack Obama is the first African American president of the United States.
Kamala Harris is of Indian and Jamaican descent."""

doc = nlp(text2)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, f'-----------[{entity.label_}]')

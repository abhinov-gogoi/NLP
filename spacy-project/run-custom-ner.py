# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("/home/abhinov/WORKSPACE/PERSONAL/NLP/model-best")

# Process whole documents
text = """
Mike my name is John Doe. 
I need to submit an insurance claim for my mother Mary Johnson.
She complained of chest discomfort and palpitations.
She is a American and lives in the U.S.A. My Father is Jew. 
Palestine are Jews. Arabs are Asians. 
MRI scan revealed a tumor in the liver.
My Wife is a Buddhist and also Chinese. Obama is African American. 
Blood test showed low levels of iron
My cvv number is two four three. And email is mike at gmail dot com. 
The Hispanic population in the United States is growing rapidly. 
The patient underwent gastric sleeve surgery for weight loss.
Barack Obama is the first African American president of the United States.
Kamala Harris is of Indian and Jamaican descent. 
She was diagnosed with epilepsy and prescribed lamotrigine.
He has a family history of breast cancer and hypertension"""

doc = nlp(text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, f'-----------[{entity.label_}]')

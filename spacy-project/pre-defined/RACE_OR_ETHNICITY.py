import spacy

# https://demos.explosion.ai/matcher

# Load a spaCy model or initialize a blank one
# nlp = spacy.blank("en")
nlp = spacy.load("en_core_web_lg")

# Define the EntityRuler with predefined words
patterns = [
    {"label": "NORP", "pattern": [{"LOWER": "american"}]},
    {"label": "NORP", "pattern": [{"LOWER": "americans"}]},
    {"label": "NORP", "pattern": [{"LOWER": "white"}]},
    {"label": "NORP", "pattern": [{"LOWER": "whites"}]},
    {"label": "NORP", "pattern": [{"LOWER": "asian"}]},
    {"label": "NORP", "pattern": [{"LOWER": "asians"}]},
    {"label": "NORP", "pattern": [{"LOWER": "african"}]},
    {"label": "NORP", "pattern": [{"LOWER": "africans"}]},
    {"label": "NORP", "pattern": [{"LOWER": "european"}]},
    {"label": "NORP", "pattern": [{"LOWER": "europeans"}]},
    {"label": "NORP", "pattern": [{"LOWER": "black"}]},
    {"label": "NORP", "pattern": [{"LOWER": "blacks"}]},
    {"label": "NORP", "pattern": [{"LOWER": "pacific Islander"}]},
    {"label": "NORP", "pattern": [{"LOWER": "pacific Islanders"}]},
    {"label": "NORP", "pattern": [{"LOWER": "latino"}]},
    {"label": "NORP", "pattern": [{"LOWER": "latinos"}]},
    {"label": "NORP", "pattern": [{"LOWER": "british"}]},
    {"label": "NORP", "pattern": [{"LOWER": "britishers"}]},
    {"label": "NORP", "pattern": [{"LOWER": "multiracial"}]},
    {"label": "NORP", "pattern": [{"LOWER": "multiracials"}]},
    {"label": "NORP", "pattern": [{"LOWER": "gaoshan"}]},
    {"label": "NORP", "pattern": [{"LOWER": "gaoshans"}]},
    {"label": "NORP", "pattern": [{"LOWER": "puerto Rican"}]},
    {"label": "NORP", "pattern": [{"LOWER": "puerto Ricans"}]},
    {"label": "NORP", "pattern": [{"LOWER": "filipino"}]},
    {"label": "NORP", "pattern": [{"LOWER": "filipinos"}]},
    {"label": "NORP", "pattern": [{"LOWER": "italian"}]},
    {"label": "NORP", "pattern": [{"LOWER": "italians"}]},
    {"label": "NORP", "pattern": [{"LOWER": "latin"}]},
    {"label": "NORP", "pattern": [{"LOWER": "jew"}]},
    {"label": "NORP", "pattern": [{"LOWER": "jews"}]},
    {"label": "NORP", "pattern": [{"LOWER": "jewish"}]},
    {"label": "NORP", "pattern": [{"LOWER": "arab"}]},
    {"label": "NORP", "pattern": [{"LOWER": "arabs"}]},
    {"label": "NORP", "pattern": [{"LOWER": "palestines"}]},
    {"label": "NORP", "pattern": [{"LOWER": "palestinian"}]},
    {"label": "NORP", "pattern": [{"LOWER": "non-Hispanic"}]},
    {"label": "NORP", "pattern": [{"LOWER": "non-Hispanics"}]},
    {"label": "NORP", "pattern": [{"LOWER": "mestizo"}]},
    {"label": "NORP", "pattern": [{"LOWER": "mestizos"}]},
    {"label": "NORP", "pattern": [{"LOWER": "yamato"}]},
    {"label": "NORP", "pattern": [{"LOWER": "yamatos"}]},
    {"label": "NORP", "pattern": [{"LOWER": "indian"}]},
    {"label": "NORP", "pattern": [{"LOWER": "indians"}]},
    {"label": "NORP", "pattern": [{"LOWER": "chinese"}]},
    {"label": "NORP", "pattern": [{"LOWER": "brown"}]},
    {"label": "NORP", "pattern": [{"LOWER": "hispanic"}]},
    {"label": "NORP", "pattern": [{"LOWER": "hispanics"}]},
    {"label": "NORP", "pattern": [{"LOWER": "mexican"}]},
    {"label": "NORP", "pattern": [{"LOWER": "mexicans"}]}
]
ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns(patterns)

# Process whole documents
text = """
Mike my name is John Doe. I need to submit an insurance claim for my mother Mary Johnson.
She is a American and lives in the U.S.A. My Father is Indian born
My Wife is a Buddhist and also Chinese. Obama is African American.
My cvv number is two four three. And email is mike at gmail dot com. 
The Hispanic population in the United States is growing rapidly.
Barack Obama is the first African American president of the United States.
Kamala Harris is of brown Indian and Jamaican descent. Indian"""
doc = nlp(text)

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, f'-----------[{entity.label_}]')

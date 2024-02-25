# https://www.youtube.com/watch?v=p_7hJvl7P2A

import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json

# Load English tokenizer, tagger, parser and NER
nlp = spacy.blank("en")
doc_bin = DocBin()

file = open("ethnicity.json")
training_data = json.load(file)
print(training_data)

for text, annotation in tqdm(training_data['annotations']):
    doc = nlp.make_doc(text)
    entities = []
    for start, end, label in annotation['entities']:
        span = doc.char_span(start, end, label=label, alignment_mode='contract')
        if span is None:
            print("Skipping entity")
        else:
            entities.append(span)
    doc.ents = entities
    doc_bin.add(doc)


doc_bin.to_disk("./training/ethnicity.spacy")

# Generate config file
# python -m spacy init config config.cfg --lang en --pipeline ner --optimize accuracy

# Start training
# python -m spacy train config.cfg --output ./ --paths.train spacy-project/training/ethnicity.spacy --paths.dev spacy-project/training/ethnicity.spacy

# Run the trained model

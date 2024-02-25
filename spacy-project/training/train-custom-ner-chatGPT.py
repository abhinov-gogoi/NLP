import spacy
from spacy.tokens import DocBin
from spacy.training import Example
import json

# Load a spaCy model or initialize a blank one
nlp = spacy.blank("en")

# JSON training data
file = open("ethnicity.json")
training_data_json = json.load(file)


# Function to create spaCy training examples from JSON
def create_training_examples(data):
    training_examples = []
    for example in data["data"]:
        text = example["text"]
        entities = example["entities"]
        doc = nlp.make_doc(text)
        spans = []
        for ent in entities:
            span = doc.char_span(ent["start"], ent["end"], label=ent["label"])
            if span is not None:
                spans.append(span)
            else:
                f"Skipping entity for text: {text}"
        training_examples.append(Example.from_dict(doc, {"entities": spans}))
    return training_examples


# Create spaCy training examples
training_examples = create_training_examples(training_data_json)

# Create a DocBin and add the training examples
doc_bin = DocBin(docs=[example.reference for example in training_examples])

# Save the DocBin to a file
doc_bin.to_disk("ethnicity.spacy")
print(f"Saved")

# Generate config file
# python -m spacy init config config.cfg --lang en --pipeline ner --optimize accuracy

# Start training
# python -m spacy train config.cfg --output ./ --paths.train spacy-project/training/ethnicity.spacy --paths.dev spacy-project/training/ethnicity.spacy

# Run the trained model
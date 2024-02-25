import spacy
from spacy.tokens import DocBin
from spacy.training import Example
import json

# Load a spaCy model or initialize a blank one
nlp = spacy.blank("en")

# JSON training data
training_data_json = {
    "data": [
        {
            "text": "Barack Obama is the first African American president of the United States.",
            "entities": [
                {
                    "start": 11,
                    "end": 25,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Kamala Harris is of Indian and Jamaican descent.",
            "entities": [
                {
                    "start": 14,
                    "end": 20,
                    "label": "RACE_OR_ETHNICITY"
                },
                {
                    "start": 25,
                    "end": 33,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "The Hispanic population in the United States is growing rapidly.",
            "entities": [
                {
                    "start": 4,
                    "end": 12,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "There is a significant Asian American community in California.",
            "entities": [
                {
                    "start": 25,
                    "end": 38,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Many Native American tribes have sovereign nations within the United States.",
            "entities": [
                {
                    "start": 5,
                    "end": 21,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Hispanic and Latino people are often used interchangeably in the United States.",
            "entities": [
                {
                    "start": 0,
                    "end": 8,
                    "label": "RACE_OR_ETHNICITY"
                },
                {
                    "start": 13,
                    "end": 18,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "There is a rich cultural diversity among African American communities.",
            "entities": [
                {
                    "start": 28,
                    "end": 44,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "The Asian American experience is multifaceted and complex.",
            "entities": [
                {
                    "start": 4,
                    "end": 20,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Native American reservations are sovereign territories within the United States.",
            "entities": [
                {
                    "start": 0,
                    "end": 15,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Indigenous peoples have a rich cultural heritage spanning thousands of years.",
            "entities": [
                {
                    "start": 0,
                    "end": 11,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "The African diaspora has contributed significantly to global culture.",
            "entities": [
                {
                    "start": 4,
                    "end": 20,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Asian Americans have faced discrimination and prejudice throughout history.",
            "entities": [
                {
                    "start": 0,
                    "end": 14,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "There is a growing awareness of Native American rights and sovereignty.",
            "entities": [
                {
                    "start": 25,
                    "end": 40,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Latinx communities in the United States are diverse and vibrant.",
            "entities": [
                {
                    "start": 0,
                    "end": 6,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "African American culture has profoundly influenced American music.",
            "entities": [
                {
                    "start": 0,
                    "end": 16,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "The Latinx population in the United States is projected to grow rapidly.",
            "entities": [
                {
                    "start": 4,
                    "end": 10,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "The Asian American community celebrates a diverse range of traditions.",
            "entities": [
                {
                    "start": 4,
                    "end": 20,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Indigenous peoples have a deep connection to the land and environment.",
            "entities": [
                {
                    "start": 0,
                    "end": 11,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Hispanic heritage is celebrated during Hispanic Heritage Month in the United States.",
            "entities": [
                {
                    "start": 0,
                    "end": 7,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "African Americans have made significant contributions to literature and art.",
            "entities": [
                {
                    "start": 0,
                    "end": 16,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "The Latinx community plays a vital role in shaping American culture.",
            "entities": [
                {
                    "start": 4,
                    "end": 10,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Asian American history is rich and diverse, spanning many centuries.",
            "entities": [
                {
                    "start": 0,
                    "end": 16,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Native American tribes have unique cultural traditions and languages.",
            "entities": [
                {
                    "start": 0,
                    "end": 15,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Hispanic Americans have roots in various countries across Latin America.",
            "entities": [
                {
                    "start": 0,
                    "end": 15,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "The African diaspora encompasses diverse cultures across the globe.",
            "entities": [
                {
                    "start": 4,
                    "end": 20,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Latino communities have a rich cultural heritage rooted in various Latin American countries.",
            "entities": [
                {
                    "start": 0,
                    "end": 6,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Asian American activists have long fought for civil rights and social justice.",
            "entities": [
                {
                    "start": 0,
                    "end": 16,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Indigenous languages are an integral part of Native American identity.",
            "entities": [
                {
                    "start": 37,
                    "end": 52,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Hispanic and Latino cultures share many common traditions and values.",
            "entities": [
                {
                    "start": 0,
                    "end": 8,
                    "label": "RACE_OR_ETHNICITY"
                },
                {
                    "start": 13,
                    "end": 18,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "The African American Civil Rights Movement had a profound impact on American society.",
            "entities": [
                {
                    "start": 4,
                    "end": 20,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Latinx artists are gaining recognition in the mainstream art world.",
            "entities": [
                {
                    "start": 0,
                    "end": 6,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Asian American literature explores themes of identity and belonging.",
            "entities": [
                {
                    "start": 0,
                    "end": 16,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Native American reservations face challenges related to economic development and healthcare.",
            "entities": [
                {
                    "start": 0,
                    "end": 15,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        },
        {
            "text": "Hispanic Americans have diverse cultural backgrounds, including Mexican, Puerto Rican, and Cuban.",
            "entities": [
                {
                    "start": 0,
                    "end": 15,
                    "label": "RACE_OR_ETHNICITY"
                }
            ]
        }
    ]
}


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

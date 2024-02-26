# pip install -U spacy
# python -m spacy download en_core_web_sm
# https://demos.explosion.ai/matcher

import spacy


# NORP: Nationalities or religious or political groups


# nlp = spacy.blank("en")
nlp = spacy.load("en_core_web_lg")

# Define the EntityRuler with predefined words
patterns = [

    # RELIGIONS
    {"label": "NORP", "pattern": [{"LOWER": "hindu"}]},
    {"label": "NORP", "pattern": [{"LOWER": "hindus"}]},
    {"label": "NORP", "pattern": [{"LOWER": "hinduism"}]},
    {"label": "NORP", "pattern": [{"LOWER": "muslim"}]},
    {"label": "NORP", "pattern": [{"LOWER": "muslims"}]},
    {"label": "NORP", "pattern": [{"LOWER": "islam"}]},
    {"label": "NORP", "pattern": [{"LOWER": "christian"}]},
    {"label": "NORP", "pattern": [{"LOWER": "christians"}]},
    {"label": "NORP", "pattern": [{"LOWER": "christianity"}]},
    {"label": "NORP", "pattern": [{"LOWER": "sikh"}]},
    {"label": "NORP", "pattern": [{"LOWER": "sikhs"}]},
    {"label": "NORP", "pattern": [{"LOWER": "sikhism"}]},
    {"label": "NORP", "pattern": [{"LOWER": "jew"}]},
    {"label": "NORP", "pattern": [{"LOWER": "jews"}]},
    {"label": "NORP", "pattern": [{"LOWER": "jewish"}]},
    {"label": "NORP", "pattern": [{"LOWER": "judaism"}]},
    {"label": "NORP", "pattern": [{"LOWER": "buddhist"}]},
    {"label": "NORP", "pattern": [{"LOWER": "buddhists"}]},
    {"label": "NORP", "pattern": [{"LOWER": "buddhism"}]},

    # NATIONALITY / RACE / ETHNICITY
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
Kamala Harris is of brown Indian and Jamaican descent and Hindu Indian.


In the quest for spiritual enlightenment, 
individuals often find themselves traversing a labyrinth of beliefs and ideologies, 
seeking solace and meaning amidst the complexities of existence. 
Take for instance, Sarah, a woman of African American descent, 
whose journey led her to explore the teachings of Buddhism, 
drawn to its emphasis on mindfulness and inner peace. 
Born and raised in a predominantly Christian community in the southern United States, 
Sarah's exploration of Buddhism ignited a profound inner dialogue, 
challenging the paradigms instilled by her upbringing. 
Despite facing skepticism and misunderstanding from some acquaintances, 
Sarah remained steadfast in her pursuit, 
delving into meditation practices and philosophical texts 
that resonated with her soul. Alongside her spiritual journey, 
Sarah found camaraderie within a diverse community of fellow seekers, 
united by their shared quest for transcendence 
beyond cultural and religious boundaries. 
Meanwhile, John, a first-generation immigrant from a Middle Eastern country, 
grappled with reconciling his Islamic heritage 
with newfound curiosity about ancient Norse mythology. 
His journey into the realm of Norse cosmology, 
with its intricate tapestry of gods and legends, 
provided him with a sense of connection to his ancestral 
roots while fostering a deeper understanding of the human 
experience. Despite encountering resistance from conservative 
family members who viewed his exploration as a betrayal of 
their traditions, John remained resolute in his pursuit of 
spiritual truth, finding solace in the wisdom gleaned from 
both Islamic and Norse sources. As Sarah and John exemplify, 
the spiritual journey transcends the confines of race, 
ethnicity, and nationality, serving as a testament to the universal 
quest for meaning and enlightenment that unites humanity across 
diverse cultures and belief systems.

In the intricate tapestry of spiritual exploration, 
individuals from various ethnic backgrounds embark on journeys 
that reflect the rich diversity of human experience. 
Consider, for instance, Maria, a multiracial woman of Latino and Italian descent, 
who finds herself drawn to the teachings of Buddhism, 
resonating deeply with its philosophy of interconnectedness and compassion. 
Raised in a predominantly Hispanic community in Los Angeles, 
Maria's journey into Buddhism represents a departure 
from the Catholic traditions of her upbringing, 
yet it also serves as a bridge to her ancestral heritage, 
incorporating elements of mindfulness into her daily life 
while honoring the cultural legacies of both her Latino and Italian roots. 
Meanwhile, across the globe in Tokyo, Hiroshi, a Yamato man, 
grapples with questions of identity and belonging 
as he explores the tenets of Judaism, intrigued by its emphasis 
on ethical living and intellectual inquiry. 
Despite being a minority in a predominantly Shinto society, 
Hiroshi's pursuit of Jewish spirituality reflects a 
universal longing for meaning and connection transcending 
ethnic boundaries, as he seeks to forge a deeper understanding of 
himself and the world around him. As Maria and Hiroshi demonstrate, 
the journey toward spiritual enlightenment is a deeply 
personal and multifaceted odyssey, encompassing individuals of 
diverse ethnicities and backgrounds who share a common 
yearning for transcendence and self-discovery.

Operator: Hello, thank you for contacting our insurance helpline. My name is Sarah, and I'll be assisting you today. May I have your name and policy number, please?
Caller: Hi Sarah, my name is John Smith, and my policy number is 123456789.
Operator: Thank you, John. How can I assist you today?
John: I'm calling because I need to update some information on my policy. I recently moved to a more diverse neighborhood, and I want to make sure my coverage reflects that.
Operator: Of course, John. We understand the importance of ensuring your policy aligns with your current circumstances. Can you please provide me with your new address and any other changes you'd like to make?
John: Sure, my new address is 123 Main Street, and I'd like to add coverage for my new car as well.
Operator: Noted, John. I see you've mentioned moving to a more diverse neighborhood. Our policies are designed to cater to individuals from various ethnic backgrounds, including Whites, Asians, Blacks, Latinos, Pacific Islanders, and those of multiracial heritage. Is there anything specific you'd like to discuss regarding your coverage in relation to your new neighborhood?
John: Actually, yes. I've noticed that there are many Puerto Rican and Filipino families in my new area, and I want to ensure that my policy provides adequate protection for any potential cultural or language barriers that may arise in case of an emergency.
Operator: That's a valid concern, John. Rest assured, our services are accessible and inclusive to individuals of all ethnicities and backgrounds, whether they are Puerto Rican, Filipino, Italian, Jewish, Arab, or any other. We also offer multilingual support to accommodate diverse linguistic needs. Is there anything else you'd like to address regarding your policy?
John: No, that covers everything. Thank you for your assistance, Sarah.
Operator: You're welcome, John. If you have any further questions or need assistance in the future, don't hesitate to reach out. Have a great day!

"""
doc = nlp(text)

print("\n\n--------------- NORP : Nationalities or religious or political groups -------------\n\n")
# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, f'-----------[{entity.label_}]')



# OUTPUT

# Mike -----------[PERSON]
# John Doe -----------[PERSON]
# Mary Johnson -----------[PERSON]
# American -----------[NORP]
# U.S.A. -----------[GPE]
# Indian -----------[NORP]
# Buddhist -----------[NORP]
# Chinese -----------[NORP]
# Obama -----------[PERSON]
# African American -----------[NORP]
# two -----------[CARDINAL]
# three -----------[CARDINAL]
# mike -----------[PERSON]
# Hispanic -----------[NORP]
# the United States -----------[GPE]
# Barack Obama -----------[PERSON]
# first -----------[ORDINAL]
# African American -----------[NORP]
# the United States -----------[GPE]
# Kamala Harris -----------[PERSON]
# brown -----------[NORP]
# Indian -----------[NORP]
# Jamaican -----------[NORP]
# Hindu Indian -----------[NORP]


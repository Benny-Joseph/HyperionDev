# Create the file garden.py for this task.
# 1. Use some Garden Path sentences or think up your own (at least 5).
# 2. Tokenise and perform Entity recognition for each of the sentences
#    after you have stored them in a list called gardenpathSentences.
# 3. See how spaCy has categorised these sentences and look up the entities you
#    don't understand
# 4. At the bottom of your file, write a comment about two unusual entities
# you found that spaCy gave one of the words of your sentences - did you expect this?

import spacy

nlp = spacy.load('en_core_web_sm')

garden_path_list = ["The old man the boat.",
                    "The complex houses married and single soldiers and their families.",
                    "The horse raced past the barn fell.",
                    "The florist sent the flowers was pleased",
                    "When Fred eats food gets thrown"]

for sample in garden_path_list:
    doc = nlp(sample)

    # Tokenisation
    print([token.orth_ for token in doc if not token.is_punct | token.is_space])

    # Entity Recognition
    nlp_sample = nlp(sample)
    print([(i, i.label_, i.label) for i in nlp_sample.ents])

''' 
The garden path sentences used in the program along with their respective Tokenizations and Entity Recognitions 
using en_core_web_sm language model are listed below: 

Garden Sentence :  "The old man the boat."
Tokenization : ['The', 'old', 'man', 'the', 'boat']
Entity Recogniion : []

Garden Sentence :  "The complex houses married and single soldiers and their families."
Tokenization : ['The', 'complex', 'houses', 'married', 'and', 'single', 'soldiers', 'and', 'their', 'families']
Entity Recogniion : []

Garden Sentence :  "The horse raced past the barn fell."
Tokenization : ['The', 'horse', 'raced', 'past', 'the', 'barn', 'fell']
Entity Recogniion : []

Garden Sentence :  "The florist sent the flowers was pleased"
Tokenization : ['The', 'florist', 'sent', 'the', 'flowers', 'was', 'pleased']
Entity Recogniion : []

Garden Sentence :  "When Fred eats food gets thrown"
Tokenization : ['When', 'Fred', 'eats', 'food', 'gets', 'thrown']
Entity Recogniion : []


When using en_core_web_md the last sentence Entity Recognition is different. It Identifies Fred as a person 
Entity Recogniion : [(Fred, 'PERSON', 380)]
'''

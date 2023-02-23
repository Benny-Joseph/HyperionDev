# Comparison of Semantic Similarity (NLP) while using sm and md language models
# Outputs for both language models given below python code

import spacy

nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

''' Output with en_core_web_md language model

0.5929930274321619
0.40415016164997786
0.22358825939615987
cat cat 1.0
cat apple 0.2036806046962738
cat monkey 0.5929930210113525
cat banana 0.2235882580280304
apple cat 0.2036806046962738
apple apple 1.0
apple monkey 0.2342509925365448
apple banana 0.6646699905395508
monkey cat 0.5929930210113525
monkey apple 0.2342509925365448
monkey monkey 1.0
monkey banana 0.4041501581668854
banana cat 0.2235882580280304
banana apple 0.6646699905395508
banana monkey 0.4041501581668854
banana banana 1.0
where did my dog go -  0.630065230699739
Hello, there is my car -  0.8033180111627156
I've lost my car in my car -  0.6787541571030323
I'd like my boat back -  0.5624940517078084
I will name my dog Diana -  0.6491444739190607


'''

'''
Output with en_core_web_sm language model


main.py:6: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(word1.similarity(word2))
0.6770565478895127
main.py:7: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(word3.similarity(word2))
0.7276309976205778
main.py:8: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(word3.similarity(word1))
0.6806929391210822
cat cat 1.0
main.py:13: UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Token.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
  print(token1.text, token2.text, token1.similarity(token2))
cat apple 0.7018378973007202
cat monkey 0.6455236077308655
cat banana 0.2214718759059906
apple cat 0.7018378973007202
apple apple 1.0
apple monkey 0.7389943599700928
apple banana 0.36197030544281006
monkey cat 0.6455236077308655
monkey apple 0.7389943599700928
monkey monkey 1.0
monkey banana 0.4232020080089569
banana cat 0.2214718759059906
banana apple 0.36197030544281006
banana monkey 0.4232020080089569
banana banana 1.0
UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.

where did my dog go -  0.4043351553824302
Hello, there is my car -  0.5648939507997681
I've lost my car in my car -  0.548028403302901
I'd like my boat back -  0.3007499696891998
I will name my dog Diana -  0.3904074310483232
'''

''' The above example shows that the md language model is far more suited to process similarity between
    longer sentences.  The sm language model can only be reliabily used to find similarity between words.'''
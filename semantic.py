# -*- coding: utf-8 -*-
"""semantic.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1csnUVdatNRaWHNPpZ8qukisCzWHhp7lm
"""

!python -m spacy download en_core_web_md

!python -m spacy download en

!python3 -m spacy download en_core_web_md

import spacy.cli
spacy.cli.download("en_core_web_md")
import en_core_web_md

nlp = en_core_web_md.load()

word_one = nlp('cat')
word_two = nlp('monkey')
word_three = nlp('banana')

print(f"{word_one}, {word_two}: {word1.similarity(word_two)}")
print(f"{word_three}, {word_two}: {word3.similarity(word_two)}")
print(f"{word_three}, {word_one}: {word3.similarity(word_one)}")

# Cat and monkey have a high similarity percentage because they animals
# banana and monkey have a low similarity percentage meaning the model isnt recognizine transive relationship bananas has with monkeys as they eat them
# banana and cat also have a low similarity percentage which is expected because banana is a fruit and cat is an animal, and cats do not eat bananas

nlp_two = en_core_web_md.load()

word1 = nlp_two('lion')
word2 = nlp_two('animal')
word3 = nlp_two('prey')

print(f"{word1}, {word2}: {word1.similarity(word2)}")
print(f"{word3}, {word2}: {word3.similarity(word2)}")
print(f"{word3}, {word1}: {word3.similarity(word1)}")

# lion and amimal have a high similiarity percentage as the model is recognizing that lion is an animal
# prey and animal have a fairly reasonable similiarity percentage because the model is recognizing that prey can be an animal that is hunted
# prey and animal also has a fairly reasonable similarity percentage because lion hunts for prey
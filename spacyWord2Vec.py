import spacy
import numpy as np
import matplotlib.pyplot as plt

nlp = spacy.load('en_core_web_lg')
repeat = True
while repeat:
    repeat = False

    exampleWord = input("What word would you like to convert to a vector? \n")
    print ("Here is ",exampleWord," as a vector")
    print (nlp('dog').vector)
    repeat = (input("\nWould you like to try another word? y/n\n") == "y")

print ("Now that we are able to turn words into vectors, we can start manipulating them")

import spacy
import numpy as np
import matplotlib.pyplot as plt

nlp = spacy.load('en_core_web_lg')
repeat = True
while repeat:
    repeat = False

    exampleWord = input("What word would you like to convert to a vector? \n")
    print ("Here is ",exampleWord," as a vector")
    exampleVector = nlp(exampleWord).vector
    print (exampleVector)
    repeat = (input("\nWould you like to try another word? y/n\n") == "y")

# Now that we are able to turn words into vectors, we can start manipulating them.
# we can measure the difference or similarity between them by their dot product
# The dot product of normalised vectors will vary between 1 and -1. 1 being identical, 0 being orthogonal (i.e unrelated), -1 being opposites
# We need to divide by the magnitude of the vectors to get the similarity
similarityWord = input("What word would you like to compare the similarity to " + exampleWord + "? \n")
similarityVector = nlp(similarityWord).vector

similarity = np.dot(exampleVector, similarityVector) / (np.linalg.norm(exampleVector) * np.linalg.norm(similarityVector))
print ("Similarity: ",similarity,"\n")

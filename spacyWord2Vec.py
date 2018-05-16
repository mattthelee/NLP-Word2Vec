import spacy 

import numpy as np
import matplotlib.pyplot as plt
nlp = spacy.load('en_core_web_lg')
print (nlp('dog').vector)

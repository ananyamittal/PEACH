import nltk
from nltk.stem import WordNetLemmatizer
lematizer = WordNetLEmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

words=[]
classes=[]
documents=[]

import nltk
nltk.download('popular')
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
import pickle 
import numpy as np 

from keras.models import load_model
model = load_model('model.h5')
import json
import random
intents = json.loads(open('data.json').read())
words = pickle.load(open('texts.pkl','rb'))
classes = pickle.load(open('labels.pkl','rb'))

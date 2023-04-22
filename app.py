import nltk
nltk.download('popular')
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
import pickle 
import numpy as np 

from keras.models import load_model
model = load_model('model.h5')

import nltk
import pandas as pd
import re
import requests
import string
import gensim
import numpy as np
import pyLDAvis.gensim
import sklearn
from gensim import corpora
from gensim.models import CoherenceModel
from matplotlib._color_data import TABLEAU_COLORS
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer
from collections import Counter
from gensim.utils import simple_preprocess
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF,LatentDirichletAllocation
from sklearn.cluster import KMeans,DBSCAN
from sklearn.manifold import TSNE
from bokeh.plotting import figure, output_file, show
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from matplotlib import pyplot as plt

#nltk.download('stopwords')
#nltk.download('words')
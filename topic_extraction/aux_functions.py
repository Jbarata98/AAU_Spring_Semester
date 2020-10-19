from imports import *

'''----------------------------------------------------------------------------------------'''

# Calculates the number of ocurrences of each of the most 10 relevant words calculated from lda model
# Prints out the output to a txt file

'''-------------printing the words and ocurrences into into a txt file from each topic------'''

def word_counter(num_topics, df, model):
    txt = ' Word {word} occurs {ocurrences:.1f} times.'
    c = 0
    d = 0
    for j in range(num_topics):
        for i in model.show_topic(topicid=j, topn=10):
            if d % 10 == 0:
                print("Topic ", c, file=open("words_houston.txt", "a"))
                c += 1
            print(txt.format(word=i[0], ocurrences=df.Tweets.str.contains(i[0]).sum()), file=open("words_houston.txt","a"))
            d += 1

'''---------------------------------------------------------------------------'''

#  THIS FUNCTION CALCULATES THE OPTIMAL NUMBER OF TOPICS FOR OUR MODEL
#  CALCULATES THE COHERENCE SCORE FOR EACH NUMBER OF TOPICS PREDETERMINED
#  PRINTS OUT A GRAPHIC WHERE WE CAN INFER THE BEST NUMBER FOR THE MODEL

'''-----------------------Computing the number of topics--------------------'''

def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    coherence_values = []
    model_list = []
    for num_passes in range(start, limit, step):
        model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=5,passes=num_passes)
        model_list.append(model)
        coherence_model_lda = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
        coherence_values.append(coherence_model_lda.get_coherence())
        print("running")
    return model_list, coherence_values

'''------------------------------------------------------------------------------------------------------'''
'''---------------------------------------------------------------------------------------------------
 #REMOVE NON ENGLISH words 1st try 
words = set(nltk.corpus.words.words())

df['Tweets'] = [" ".join(w for w in nltk.wordpunct_tokenize(x)
                       if w.lower() in words or not w.isalpha())
                       for x in df['Tweets']]
                       
 
DICTIONARY_URL = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
FILTER_COLUMN_NAME = 'Tweets'
PRINTABLES_SET = set(string.printable)

def is_english_printable(word):
    return PRINTABLES_SET >= set(word)

def prepare_dictionary(url):
    return set(requests.get(url).text.splitlines())

DICTIONARY = prepare_dictionary(DICTIONARY_URL)

df = df[df[FILTER_COLUMN_NAME].map(is_english_printable) &
        df[FILTER_COLUMN_NAME].map(str.lower).isin(DICTIONARY)]
----------------------------------------------------------------------------------------------------------'''

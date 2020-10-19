'''-------------------------------------------------------------------------------------------------------------------------'''

# This file preprocessed the data removing all the non relevant words, tokenizing, etc

'''--------------------------------------Loading the file and preparing it for further manipulation--------------------------'''

from imports import *

f = open('bag.txt', 'r')
answer = {}
for line in f:
    k, v = line.strip().split(': ')
    answer[k.strip()] = v.strip()

f.close()

data_dict = answer
data_items = data_dict.items()
data_list = list(data_items)

df = pd.DataFrame(data_list)  #convert into a pandas dataframe for easier manipulation

df.rename(columns={0: 'Nr', 1: 'Tweets'}, inplace=True) #rename the columns for easier understanding

'''-------------------------------------------------------------------------------------------------------------------------'''

# This sections takes care of the preprocessing
# clean tweets function removes all the users like '@joao',removes urls, accepts only alphanumeric,lower cases and tokenizes the words
#
'''--------------------------PREPROCESSING-----------------------------------------------------------------------------------'''


def clean_tweets(tweet):
    user_removed = re.sub(r'@[A-Za-z0-9]+', '', tweet)
    link_removed = re.sub(r"http\S+", '', user_removed)
    only_alphanumeric = re.sub('[^a-zA-Z0-9]', ' ', link_removed)
    lower_case_tweet = only_alphanumeric.lower()
    tok = WordPunctTokenizer()
    words = tok.tokenize(lower_case_tweet)
    clean_tweet = (' '.join(words)).strip()
    return clean_tweet

df['Tweets'] = df['Tweets'].apply(clean_tweets)  #applies the function above

#FURTHER PREPROCESSING

df['Tweets'] = df['Tweets'].str.replace(r'\d+', '')           # removes numbers
df['Tweets'] = df['Tweets'].str.replace(r'\b(\w{0,3})\b', '') # removes all words with less than 3 characters
df['Tweets'] = df['Tweets'].replace(r'\s+', ' ', regex=True)  # removes spaces
df['Tweets'] = df['Tweets'].str.replace('', '')


#Removes all non english words from corpus
words = set(nltk.corpus.words.words())

stop = open('twitter-stopwords.txt', 'r')
stopwords_txt = stop.readlines()
stopwords= [x.replace('\n', '') for x in stopwords_txt]
stopwords = set(stopwords)


f = lambda x: " ".join(x for x in x.split() if x not in stopwords) #should remove stopwords
df['Tweets'] = df['Tweets'].apply(f)


#this function removes white spaces I still had on the dataset
df['Tweets'] = df['Tweets'].str.strip()
filter = df["Tweets"] != ""
df = df[filter]

#df.drop_duplicates(subset='Tweets', inplace = True)


old_df = df.copy()  #saving the old dataframe before LDA changes it for further manipulation on the word_counter function

'''---------------------------VISUALIZATION-------------------------------------------------------------'''

df.to_csv(r'out_preprocessed.csv', index=False)
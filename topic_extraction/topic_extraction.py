from imports import *
import aux_functions as aux
import data_preparation as data

'''----------------------------------------------------------------------------------------------------'''
# This is where LDA does its magic, verify LDA documentation if you have any doubts on the procedure
# 1st - make a dictionary
# 2nd - make bow that  assigns each word to an id and has its number of ocurrences in that tweet
# 3rd  - mathematical lda magic
# 4th - evaluation of the model

'''------------------------------------------------------------LDA----------------------------------------------------'''
 # this variable is necessary just for the word counter function

data.df["Tweets"] = data.df["Tweets"].map(lambda x: x.split(' '))

dictionary = corpora.Dictionary(data.df["Tweets"])

data.df["bow"] = data.df["Tweets"].map(dictionary.doc2bow)

def compute_lda(corpus,id2word,dataframe,ntopics):
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                id2word=id2word,
                                                num_topics=ntopics,
                                                passes = 50,
                                                alpha='auto',
                                                per_word_topics=True)

    #print(*lda_model.print_topics(), sep ='\n')   #visualization of the how the lda calculates the weights for each words, uncomment to visualize

    coherence_model_lda = CoherenceModel(model=lda_model, texts=data.df['Tweets'], dictionary=dictionary, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()  #coherence value of the current model

    print('\nCoherence: ', coherence_lda) #higher , the better but it depends on human interpretation aswell
    print('\nPerplexity: ', lda_model.log_perplexity(dataframe['bow']))  # a measure of how good the model is. lower the better.
    topics = lda_model.print_topics(num_words=10)
    for topic in topics:
        print(topic)
    return lda_model

lda = compute_lda(data.df["bow"],dictionary,data.df,5)

'''----------------------------------------------------------------------------------------------------'''

# CLUSTERING SECTION BELOW USES DBSCAN AND TSNE ,TO RUN JUST UNCOMMENT THE TECHNIQUE YOU WANT

# THE HYPERPARAMETERS ARE NOT FINELY TUNED , WORK IN PROGRESS

'''-----------------------------------------------DBSCAN --------------------------------------------------

# Get topic weights
topic_weights = []
for i, row_list in enumerate(lda[data.df['bow']]):
    topic_weights.append([w for i, w in row_list[0]])

arr = pd.DataFrame(topic_weights).fillna(0).values
# Keep the well separated points (optional)

arr = arr[np.amax(arr, axis=1) > 0.35]

# Dominant topic number in each doc
topic_num = np.argmax(arr, axis=1)


data = StandardScaler().fit_transform(arr)

dbscan = DBSCAN(eps = 0.5, min_samples= 8)

dbscan.fit(data)
mycolors = np.array([color for name, color in TABLEAU_COLORS.items()])

data_pred = dbscan.fit_predict(data)

plt.scatter(data[:,0], data[:,1],color=mycolors[topic_num])
plt.title("DBSCAN")
plt.show()

-----------------------------------------------------------------------------------------------------------'''

'''---------------------------------------------- TSNE ----------------------------------------------------'''

# Get topic weights
topic_weights = []
for i, row_list in enumerate(lda[data.df['bow']]):
    topic_weights.append([w for i, w in row_list[0]])


arr = pd.DataFrame(topic_weights).fillna(0).values
# Keep the well separated points (optional)
print(arr)
arr = arr[np.amax(arr, axis=1) > 0.35]

# Dominant topic number in each doc
topic_num = np.argmax(arr, axis=1)

# tSNE Dimension Reduction
tsne_model = TSNE(n_components=2, perplexity= 10, verbose=1, random_state=0, angle=.99, init='pca')
tsne_lda = tsne_model.fit_transform(arr)

n_topics = 5
mycolors = np.array([color for name, color in TABLEAU_COLORS.items()])
plot = figure(title="t-SNE Clustering of {} LDA Topics".format(n_topics),
              plot_width=900, plot_height=700)
plot.scatter(x=tsne_lda[:,0], y=tsne_lda[:,1], color=mycolors[topic_num])
show(plot)

'''------------------------------------------------------------------------------------------------------'''

'''---------------------------VISUALIZATION-------------------------------------------------------------
#num_topics = 20

#lda_models = []
#for i in range(num_topics+1):
 #   lda = compute_lda(data.df["bow"],dictionary,data.df,num_topics)
   # lda_models.append(lda)

#vis = pyLDAvis.gensim.prepare(lda, data.df['bow'], dictionary) #LDA visualization tool
#pyLDAvis.save_html(vis, 'LDA_Visualization.html')

data.df.to_csv(r'out_final.csv', index=False)  # FINAL CSV FILE FOR VISUALIZATION PURPOSES (TWEETS AND BOW)

txt = "With {ntopics} topics we have this distribution:"

#topic_numbers_list = [5,10,15,20]
#for n in range(num_topics+1):
 #   if n in topic_numbers_list:
  #      print(txt.format(ntopics=n), file=open("words_houston.txt", "a"))
   #     print("\n",file=open("words_houston.txt", "a"))
    #    aux.word_counter(n,data.old_df,lda_models[n])  #this function writes to a txt file the words and occurences but be careful it keeps writing
                                                     #delete the words.txt always if u want to try it again to prevent it duplicate writing

#the following is to plot the optimal k topics value graphic uncomment the coherence_values function above and the following code to calculate

aux.word_counter(5,data.old_df,lda)  #this function writes to a txt file the words and occurences but be careful it keeps writing

---------------------------------------------------------------------------------------------------

model_list, coherence_values = aux.compute_coherence_values(dictionary=dictionary, corpus=data.df['bow'], texts=data.df['Tweets'], start=1, limit=100, step=20)

limit=100; start=1; step=20;
x = range(start, limit, step)
plt.plot(x, coherence_values,label = "")
plt.title("C_V per number of passes")
plt.xlabel("Num Passes")
plt.ylabel("Coherence score")
plt.show()
----------------------------------------------------------------------------------------------------'''
from topic_extraction import *
import data_preparation_geotagged as data_geo

num_topics = 2


data_geo.df["Tweets"] = data_geo.df["Tweets"].map(lambda x: x.split(' '))

dictionary = corpora.Dictionary(data_geo.df["Tweets"])

data_geo.df["bow"] = data_geo.df["Tweets"].map(dictionary.doc2bow)


data_geo.df.to_csv(r'out_preprocessed_geo.csv', index=False)

#length = len(data_geo.df)
#split = length//length

#for j in range(len(data_geo.df["bow"])):
    #for i in range(len(data_geo.df.loc[j,"bow"])):
        #print(data_geo.df.loc[i, "bow"][:split])

#print(data_geo.df["bow"])


lda = compute_lda(data_geo.df["bow"].iloc[:3],dictionary,data_geo.df)

print(data_geo.df["bow"].iloc[:3])
#aux.word_counter(num_topics,data_geo.old_df_geo,lda)
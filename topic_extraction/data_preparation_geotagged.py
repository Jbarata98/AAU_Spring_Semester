from data_preparation import *

with open('geotagged.txt', 'r') as f:
    x = f.readlines()

new_string = x[0].replace('[', "")
y = new_string.replace('(', "")
lel = y.replace('WordList', "")

s = lel.split('])')


print(x)
print(s[0])
dictOfWords = { i : s[i] for i in range(0, len(s) ) }

print(dictOfWords[0])
s = dictOfWords[0].split('])')
data_items = dictOfWords.items()
data_list = list(data_items)







print(data_list)
df = pd.DataFrame(data_list)


df.rename(columns={0: 'Cities', 1: 'Tweets'}, inplace=True)


#for col in df.columns:
    #print(col)
df.to_csv(r'df_geotagged_before', index=False)

#df['Tweets'] = df['Tweets'].apply(clean_tweets)
#further_preprocessing(df)


#old_df_geo = df.copy()

#df.to_csv(r'df_geotagged', index=False)

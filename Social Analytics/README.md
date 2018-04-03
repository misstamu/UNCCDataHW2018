
# News Mood via Twitter

#Observations:
    
The latest overall sentiment from the news sources analyzing the last 100 tweets is negative except from CNN.
    
BBC which had a greater negative sentiment compared to the other also had more tweets discussing broad international news.
    
Although the latest Fox News tweets mainly centered around POTUS Trump, it's negative sentiment was low. It may correspond to the latest bump in his approval ratings.


```python
#Dependencies
import tweepy
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

from config import consumer_key, consumer_secret, access_token, access_token_secret
```


```python
# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
```


```python
# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret
```


```python
# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
target_terms = ("@BBC", "@CBSNews", "@CNN", "@FoxNews", "@nytimes")

# Variables for holding values 
source = []
tweet_times = []
tweet_text = []
compound_list = []
positive_list = []
negative_list = []
neutral_list = []

# Loop through all target users
for target in target_terms:
    
      # Run search around each tweet
        public_tweets = api.search(target, count=100, result_type="recent")

        # Loop through all tweets
        for tweet in public_tweets["statuses"]:
            
            source.append(target)
            raw_time = tweet["created_at"]
            tweet_times.append(raw_time)
                
            txt = tweet["text"]
            tweet_text.append(txt)
           
            # Run Vader Analysis on each tweet
            compound = analyzer.polarity_scores(tweet["text"])["compound"]
            pos = analyzer.polarity_scores(tweet["text"])["pos"]
            neu = analyzer.polarity_scores(tweet["text"])["neu"]
            neg = analyzer.polarity_scores(tweet["text"])["neg"]

            # Add each value to the appropriate array
            compound_list.append(compound)
            positive_list.append(pos)
            negative_list.append(neg)
            neutral_list.append(neu)


```


```python
#create dataframe of all values
tweet_df = pd.DataFrame({'Source':source,'Time':tweet_times,'Tweet Text':tweet_text,'Compound':compound_list,
                         'Positive':positive_list,'Neutral':neutral_list,'Negative':negative_list})
tweet_df = tweet_df[['Source','Compound','Negative','Neutral','Positive','Time','Tweet Text']]

# Save data to csv
tweet_df.to_csv("NewsTweet Sentiment.csv")
tweet_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Source</th>
      <th>Compound</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Time</th>
      <th>Tweet Text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>@BBC</td>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Mon Apr 02 13:10:30 +0000 2018</td>
      <td>RT @corpodelledonne: La @BBC applicherà il 50/...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>@BBC</td>
      <td>-0.3182</td>
      <td>0.173</td>
      <td>0.726</td>
      <td>0.101</td>
      <td>Mon Apr 02 13:10:16 +0000 2018</td>
      <td>RT @PhyllisMufson: "Picked the wrong career?" ...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>@BBC</td>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Mon Apr 02 13:10:15 +0000 2018</td>
      <td>@censorsapproved That’s asking a bit much. Thi...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>@BBC</td>
      <td>0.1477</td>
      <td>0.119</td>
      <td>0.740</td>
      <td>0.141</td>
      <td>Mon Apr 02 13:10:14 +0000 2018</td>
      <td>RT @needsfixingnow: @RCorbettMEP Wow British m...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>@BBC</td>
      <td>0.0000</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Mon Apr 02 13:10:14 +0000 2018</td>
      <td>@drkerem @Noor_and_Alaa @RedCrescentTR @UNReli...</td>
    </tr>
  </tbody>
</table>
</div>




```python
tweet_df['Source'].value_counts()
```




    @BBC        100
    @CBSNews    100
    @FoxNews    100
    @CNN        100
    @nytimes    100
    Name: Source, dtype: int64




```python
bbc = tweet_df.query('Source == "@BBC"')
bbcx = pd.Series(np.arange(bbc['Compound'].count(), 0, -1))
bbcy = np.array(bbc['Compound'])

cbs = tweet_df.query('Source == "@CBSNews"')
cbsx = pd.Series(np.arange(cbs['Compound'].count(), 0, -1))
cbsy = np.array(cbs['Compound'])

fox = tweet_df.query('Source == "@FoxNews"')
foxx = pd.Series(np.arange(fox['Compound'].count(), 0, -1))
foxy = np.array(fox['Compound'])

cnn = tweet_df.query('Source == "@CNN"')
cnnx = pd.Series(np.arange(cnn['Compound'].count(), 0, -1))
cnny = np.array(cnn['Compound'])

nyt = tweet_df.query('Source == "@nytimes"')
nytx = pd.Series(np.arange(nyt['Compound'].count(), 0, -1))
nyty = np.array(nyt['Compound'])
```


```python
#formatted today's date for charts
tdate = dt.datetime.today().strftime("%m/%d/%Y")
```

# Sentiment Analysis Scatter Plot


```python
bbcp = plt.scatter(bbcx, bbcy, s=100, c='blue', edgecolors="black", label='BBC')
cbsp = plt.scatter(cbsx, cbsy, s=100, c='red', edgecolors="black", label='CBS')
foxp = plt.scatter(foxx, foxy, s=100, c='green', edgecolors="black", label='FOX')
cnnp = plt.scatter(cnnx, cnny, s=100, c='yellow', edgecolors="black", label='CNN')
nytp = plt.scatter(nytx, nyty, s=100, c='purple', edgecolors="black", label='New York Times')

plt.title("Sentiment Analysis of News Media Tweets " + str(tdate))
plt.xlabel("Tweets Ago")
plt.ylabel("Tweet Polarity")
plt.xlim([105,0])
plt.grid(True)
plt.legend(handles=[bbcp,cbsp,foxp,cnnp,nytp], loc="right", bbox_to_anchor=(1.4, 0.8))
plt.savefig("News Sentiment Plot.png")
plt.show()
```


![png](output_12_0.png)



```python
newsorg = ["BBC", "CBS", "FOX", "CNN", "New York Times"]
cmdavg = [np.mean(bbcy),np.mean(cbsy),np.mean(foxy),np.mean(cnny),np.mean(nyty)]
x_axis = np.arange(len(cmdavg))
```

# Overall Media Sentiment Bar Plot


```python
colors = ["blue","red","green","yellow","purple"]
plt.bar(x_axis, cmdavg,color=colors, align="edge")

tick_locations = [value+0.4 for value in x_axis]
plt.xticks(tick_locations, newsorg)

plt.title("Overall Media Sentiment based on Twitter " + str(tdate))
plt.ylabel("Tweet Polarity")
plt.savefig("News Twitter Sentiment.png")
plt.show()
```


![png](output_15_0.png)


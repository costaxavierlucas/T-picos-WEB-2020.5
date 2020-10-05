import tweepy as tw
import pandas as pd

with open('chavesdeacesso.txt', 'r') as tfile:
    consumer_key = tfile.readline().strip('\n')
    consumer_secret = tfile.readline().strip('\n')
    access_token = tfile.readline().strip('\n')
    access_token_secret = tfile.readline().strip('\n')

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

query_search = '#pandemia' + '-filter:retweets'

tweets_dict = {}

cursor_tweets = tw.Cursor(api.search, q=query_search).items(1)
for tweet in cursor_tweets:
    twkeys = tweet._json.keys()
    tweets_dict = tweets_dict.fromkeys(twkeys)
    for key in tweets_dict.keys():
        try:
            twkey = tweet._json[key]
            tweets_dict[key].append(twkey)
        except KeyError:
            twkey = ""
            tweets_dict[key].append("")
        except:
            tweets_dict[key] = [twkey]
        print('tweets_dict[key]: {} - tweet[key]: {}'.format(tweets_dict[key], twkey))
       
dfTweets = pd.DataFrame.from_dict(tweets_dict)
dfTweets.to_csv("COVIDtwitter.csv", index=False)

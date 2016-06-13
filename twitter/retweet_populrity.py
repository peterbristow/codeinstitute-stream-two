import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter


CONSUMER_KEY = 'WDuWJHE6vnwRHkTT5iC7EkBhn'
CONSUMER_SECRET = '3ojh9qaUXXuVT0aZ2j6D5Zk0IUnEGHCXvVewUft1LYXi6Sevsb'
OAUTH_TOKEN = '719250597564846084-Q0rrfI2DwoZM60oPm31XmXV9EzQoLbV'
OAUTH_TOKEN_SECRET = 'qWuYy5jJB8w2zdMhXA8tM26ZqAnTqYFl1zw0vutPnOS78'


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 150
query = 'Ireland'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

min_retweets =  10 # the min amount of times a status is retweeted to gain entry to our list.
                   # reset this value to suit your own tests

pop_tweets = [ status
            for status in results
                if status._json['retweet_count'] > min_retweets ]

# create a dictionary of tweet text and associated re tweets
tweets_tup = tuple([(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count']) for tweet in pop_tweets])

# remove any duplicates
pop_tweets_set = set(tweets_tup)

# Sort the tuple entries in descending order
sorted_tweets_tup = sorted(pop_tweets_set, key=itemgetter(1), reverse=True)[:5]

# prettify
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in sorted_tweets_tup:
   table.add_row([key, val])
   table.max_width['Text'] = 50
   table.align['Text'], table.align['Retweet Count'] = 'l', 'r' # align the columns
print table

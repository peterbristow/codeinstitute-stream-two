import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'WDuWJHE6vnwRHkTT5iC7EkBhn'
CONSUMER_SECRET = '3ojh9qaUXXuVT0aZ2j6D5Zk0IUnEGHCXvVewUft1LYXi6Sevsb'
OAUTH_TOKEN = '719250597564846084-Q0rrfI2DwoZM60oPm31XmXV9EzQoLbV'
OAUTH_TOKEN_SECRET = 'qWuYy5jJB8w2zdMhXA8tM26ZqAnTqYFl1zw0vutPnOS78'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

# print json.dumps(dub_trends, indent=1)
# print json.dumps(lon_trends, indent=1)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print common_trends

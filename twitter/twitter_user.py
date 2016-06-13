# coding=utf-8
import tweepy
from tweepy import OAuthHandler

# Replace these values with our own twitter app settings
CONSUMER_KEY = 'WDuWJHE6vnwRHkTT5iC7EkBhn'
CONSUMER_SECRET = '3ojh9qaUXXuVT0aZ2j6D5Zk0IUnEGHCXvVewUft1LYXi6Sevsb'
OAUTH_TOKEN = '719250597564846084-Q0rrfI2DwoZM60oPm31XmXV9EzQoLbV'
OAUTH_TOKEN_SECRET = 'qWuYy5jJB8w2zdMhXA8tM26ZqAnTqYFl1zw0vutPnOS78'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

# user = api.get_user('@madonna')
#
# print(user.screen_name)
# print(user.followers_count)
#
# for friend in user.friends():
#     print
#     print(friend.screen_name)
#     print(friend.followers_count)

# harvest tweets that appear on a user’s timeline
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print(status.text)

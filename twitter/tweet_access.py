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

count = 10
query = 'Dublin'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

# for result in results:
#     print result

# for result in results:
#     print json.dumps(result._json, indent=2)

print json.dumps(results[0]._json, indent=4)

for status in results:
    print status.text.encode('utf-8')
    print status.user.id
    print status.user.screen_name
    print status.user.profile_image_url_https
    print status.user.followers_count
    print status.place
import json
import pandas as panda
import matplotlib.pyplot as plt
import re

tweets_data_path = 'tweet_mining.json'


def read_json(file_path):
    results = []
    tweets_file = open(file_path, "r")
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue
    return results


def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False


results = read_json(tweets_data_path)

# create  a dataframe
statuses = panda.DataFrame()

# store the text values
statuses['text'] = map(lambda status: status['text'], results)
# store the language values
statuses['lang'] = map(lambda status: status['lang'], results)
# sometimes there may not be a 'place' listed in the tweet , so set to 'None' if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

# new DataFrame columns
statuses['python'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('python', status))
statuses['java'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('java', status))
statuses['c#'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('c#', status))
statuses['ruby'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('ruby', status))

# output the number of tweets where it is True that they contain our keywords
print statuses['python'].value_counts()[True]
print statuses['java'].value_counts()[True]
print statuses['c#'].value_counts()[True]
print statuses['ruby'].value_counts()[True]

slices = [
    statuses['python'].value_counts()[True],
    statuses['java'].value_counts()[True],
    statuses['c#'].value_counts()[True],
    statuses['ruby'].value_counts()[True]
]

languages = ['python', 'java', 'c#', 'ruby']

# slices = [7,2,2,13]
# activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=languages,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0.1, 0.1, 0.1, 0.1),
        autopct='%1.1f%%')

plt.title('Tweet count of each keyword\nCheck this out')
plt.show()

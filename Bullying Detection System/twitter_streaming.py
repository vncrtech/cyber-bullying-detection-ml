"""
The code below was heavily based on the tutorial found in http://socialmedia-class.org/twittertutorial.html

The code was modified to extract tweets that were made in the Philippines.
"""

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Import Pandas
import pandas as pd

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# filtered by Philippine location
# coordinates were determined using http://boundingbox.klokantech.com/
iterator = twitter_stream.statuses.filter(locations="116.982421875,5.4847680181,127.001953125,18.7295019991")

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
tweet_count = 1000

text, follower_count, statuses_count, friends_count, profile_image_url, \
name, screen_name, country_code, coordinates = ([] for i in range(9))

for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We store the value of the response into an array and add it to a dataframe
    # print json.dumps(tweet)

    if 'text' in tweet:
        name.append(tweet['user']['name'])
        screen_name.append(tweet['user']['screen_name'])
        text.append(tweet['text'])
        follower_count.append(tweet['user']['followers_count'])
        statuses_count.append(tweet['user']['statuses_count'])
        friends_count.append(tweet['user']['friends_count'])
        profile_image_url.append(tweet['user']['profile_image_url'])
        country_code.append(tweet['place']['country_code'])
        coordinates.append(tweet['place']['bounding_box']['coordinates'])

    name_pd = pd.DataFrame(name)
    screen_name_pd = pd.DataFrame(screen_name)
    text_pd = pd.DataFrame(text)
    follower_count_pd = pd.DataFrame(follower_count)
    statuses_count_pd = pd.DataFrame(statuses_count)
    friends_count_pd = pd.DataFrame(friends_count)
    profile_image_url_pd = pd.DataFrame(profile_image_url)
    country_code_pd = pd.DataFrame(country_code)
    coordinates_pd = pd.DataFrame(coordinates)

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
    print tweet_count

    if tweet_count <= 0:
        break

cleaned_tweets = pd.concat([name_pd, screen_name_pd, text_pd, follower_count_pd, statuses_count_pd, \
                            friends_count_pd, profile_image_url_pd, country_code_pd, coordinates_pd], axis=1)
cleaned_tweets.columns = ['Name', 'Screen Name', 'Text', 'Follower Count', 'Statuses Count', 'Friends Count', \
                          'Profile Image URL', 'Country Code', 'Coordinates']

cleaned_tweets.to_csv('tweets.csv', encoding='utf-8')
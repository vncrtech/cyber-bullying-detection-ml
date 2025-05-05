"""
The code below was heavily based on the tutorial found in http://socialmedia-class.org/twittertutorial.html

The code was modified to extract tweets that were made in the Philippines.
"""

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Import Pandas and Folium
import pandas as pd
import folium

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
iterator = twitter_stream.statuses.filter(
    locations="116.982421875,5.4847680181,127.001953125,18.7295019991")

# set the number of tweets you want to get
tweet_count = 100

text, follower_count, statuses_count, friends_count, profile_image_url, \
    name, screen_name, country_code, lat, lon = ([] for i in range(10))

for tweet in iterator:
    tweet_count -= 1
    # We store the value of the response into an array
    if 'text' in tweet:
        name.append(tweet['user']['name'])
        screen_name.append(tweet['user']['screen_name'])
        text.append(tweet['text'])
        follower_count.append(tweet['user']['followers_count'])
        statuses_count.append(tweet['user']['statuses_count'])
        friends_count.append(tweet['user']['friends_count'])
        profile_image_url.append(tweet['user']['profile_image_url'])
        country_code.append(tweet['place']['country_code'])
        lat.append(str(tweet['place']['bounding_box']['coordinates']).split("],")[
                   0].split(',')[1].strip('['))
        lon.append(str(tweet['place']['bounding_box']['coordinates']).split("],")[
                   0].split(',')[0].strip('['))

    print(tweet_count)

    if tweet_count <= 0:
        break

# Save the arrays into a DataFrame
name_pd = pd.DataFrame(name)
screen_name_pd = pd.DataFrame(screen_name)
text_pd = pd.DataFrame(text)
follower_count_pd = pd.DataFrame(follower_count)
statuses_count_pd = pd.DataFrame(statuses_count)
friends_count_pd = pd.DataFrame(friends_count)
profile_image_url_pd = pd.DataFrame(profile_image_url)
country_code_pd = pd.DataFrame(country_code)
lat_pd = pd.DataFrame(lat)
lon_pd = pd.DataFrame(lon)

# Combine all DataFrames into a single DataFrame
cleaned_tweets = pd.concat([name_pd, screen_name_pd, text_pd, follower_count_pd, statuses_count_pd,
                            friends_count_pd, profile_image_url_pd, country_code_pd, lat_pd, lon_pd], axis=1)
cleaned_tweets.columns = ['Name', 'Screen Name', 'Text', 'Follower Count', 'Statuses Count', 'Friends Count',
                          'Profile Image URL', 'Country Code', 'Lat', 'Lon']

# Save DataFrame to csv
cleaned_tweets.to_csv('tweets.csv', encoding='utf-8')

cleaned_tweets = pd.read_csv('tweets.csv')

# Set the position of Folium map
map_object = folium.Map(location=[13, 122], zoom_start=6)

# Plot the Tweets in the map
for lat, lon, text in zip(cleaned_tweets['Lat'], cleaned_tweets['Lon'], cleaned_tweets['Text']):
    map_object.add_child(folium.Marker(
        location=[lat, lon], popup=(folium.Popup(text))))

# Save map into an HTML file
folium.Map.save(map_object, "index.html")

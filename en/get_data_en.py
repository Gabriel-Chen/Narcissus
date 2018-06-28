from keys import *
import tweepy
from time import sleep
import json
import re
import csv

# twitter credential
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

def retrieve_tweets_key (key):
    feed = open(key + '.json', 'r')
    data_list = json.load(feed)
    feed.close()
    for status in tweepy.Cursor(api.search, q=key).items(10):
        print('successfully retrieved! ')
        print(status.coordinates)
        data_list.append(status._json)
        sleep(1)
    json.dump(data_list, out_file)
    out_file = open(key + '.json', 'w')
    out_file.close()
    return data_list

def retrieve_tweets (key_word):
    print(key_word)
    #feed = open(key_word + '.json', 'r')
    data_list = [ ] #json.load(feed)
    #feed.close()
    for status in tweepy.Cursor(api.search, q=key_word).items(50):
        print("successfully retrieved!")
        data_list.append(status._json)
        sleep(1)
    out_file = open(key_word + '.json', 'w')
    json.dump(data_list, out_file)
    out_file.close()
    return data_list

def feed_keywords ():
    words_sheet = open('key_words_en.json', 'r')
    feed = json.load(words_sheet)
    for item in feed:
        key_word = item['Environmental Keywords in English']
        retrieve_tweets(key_word)
    return True

if __name__ == "__main__":
    feed_keywords()
    #retrieve_tweets_key('water pollution')

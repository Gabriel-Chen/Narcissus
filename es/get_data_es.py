from keys import *
import tweepy
from time import sleep
import json
import re

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
    try:
        feed = open(key_word + '.json', encoding='latin-1', mode='r')
        data_list = json.load(feed)
        feed.close()
    except:
        data_list = [ ]
    for status in tweepy.Cursor(api.search, q=key_word).items(100):
        print("successfully retrieved!")
        data_list.append(status._json)
        sleep(1)
    out_file = open(key_word + '.json', encoding='latin-1', mode='w')
    json.dump(data_list, out_file)
    out_file.close()
    return data_list

def feed_keywords ():
    words_sheet = open('key_words_es.json', encoding='latin-1', mode='r')
    reader = json.load(words_sheet)
    for item in reader:
        key_word = item['Environmental Keywords in Spanish']
        retrieve_tweets(key_word)
    return True

if __name__ == "__main__":
    feed_keywords()
    #retrieve_tweets_key('water pollution')

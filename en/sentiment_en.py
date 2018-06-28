import json
import re
from textblob import TextBlob

def clean_data (text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split())

def get_sentiment (polarity):
    if polarity > 0:
        return 'positive'
    if polarity == 0:
        return 'neutral'
    return 'negative'

def add_sentiment (feed):
    f = open(feed + '.json', 'r')
    data = json.load(f)
    f.close()
    for item in data:
        text = item['text']
        text = clean_data(text)
        testimonial = TextBlob(text)
        polarity = testimonial.sentiment.polarity
        item['marker-color'] = "#718ad8"
        if polarity < 0:
            item['marker-color'] = "#F36170"
    f = open(feed + '.json', 'w')
    json.dump(data, f)

if __name__ == "__main__":
    add_sentiment("data_loc_en")

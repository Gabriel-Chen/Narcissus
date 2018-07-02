import json
import re
from textblob import TextBlob
from googletrans import Translator

# googletrans set up
translator = Translator()

def clean_data (text):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split())

def add_sentiment (feed):
    f = open(feed + '.json', encoding='latin-1', mode='r')
    data = json.load(f)
    f.close()
    for item in data:
        text = item['text']
        text = clean_data(text)
        text_eng =  translator.translate(text).text
        testimonial = TextBlob(text_eng)
        polarity = testimonial.sentiment.polarity
        item['marker-color'] = "#718ad8"
        if polarity < 0:
            item['marker-color'] = "#F36170"
    f = open(feed + '.json', encoding='latin-1', mode='w')
    json.dump(data, f)

if __name__ == "__main__":
    add_sentiment("data_loc_es")

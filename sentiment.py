import json

def add_sentiment (feed):
    data = json.load(open(feed + '.json', 'r'))
    text = data['features'][0]['properties']['text']


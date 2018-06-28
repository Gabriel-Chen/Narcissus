import json

words_sheet = open('key_words_en.json', 'r')
try:
    reader = json.load(words_sheet)
    words_sheet.close()
    for item in reader:
        key_word = item['Environmental Keywords in English']
        symbol = item['symbol']
        f = open(key_word + '.json', 'r')
        gf = json.load(f)
        f.close()
        for tweet in gf:
            tweet['marker-symbol'] = symbol
        f = open(key_word + '.json', 'w')
        json.dump(gf, f)
except:
    words_sheet.close()

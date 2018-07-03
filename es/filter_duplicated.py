import json

word_sheet = open('key_words_es.json', encoding='latin-1', mode='r')
reader = json.load(word_sheet)
word_sheet.close()
for data in reader:
    word = data['Environmental Keywords in Spanish']
    f = open(word + '.json', encoding='latin-1', mode='r')
    jf = json.load(f)
    f.close()
    seen = set()
    l = [ ]
    for item in jf:
        if item['id'] not in seen:
            seen.add(item['id'])
            l.append(item)
    f = open(word + '.json', encoding='latin-1', mode='w')
    json.dump(l, f)

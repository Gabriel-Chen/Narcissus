import json

word_sheet = open('key_words_en.json', 'r')
reader = json.load(word_sheet)
word_sheet.close()
for data in reader:
    word = data['Environmental Keywords in English']
    f = open(word + '.json', 'r')
    jf = json.load(f)
    f.close()
    seen = set()
    l = [ ]
    for item in jf:
        if item['id'] not in seen:
            seen.add(item['id'])
            l.append(item)
    f = open(word + '.json', 'w')
    json.dump(l, f)

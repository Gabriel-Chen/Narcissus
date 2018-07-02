import json

def get_data_with_loc(key_word, symbol, data_list):
    f = open(key_word + '.json', 'r')
    jf = json.load(f)
    for item in jf:
        if item['coordinates']:
            item['marker-symbol'] = symbol
            data_list.append(item)
    return data_list


def feed_keywords (out_f):
    data_list = [ ]
    out_f = open(out_f + '.json', encoding='latin-1', mode='w')
    words_sheet = open('key_words_es.json', encoding='latin-1', mode='r')
    reader = json.load(words_sheet)
    words_sheet.close()
    for item in reader:
        key_word = item['Environmental Keywords in Spanish']
        symbol = item['symbol']
        data_list = get_data_with_loc(key_word, symbol, data_list)
    json.dump(data_list, out_f)
    out_f.close()
    return True

if __name__ == "__main__":
    feed_keywords('data_loc_es')

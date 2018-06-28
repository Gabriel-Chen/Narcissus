import csv
import json

def get_data_with_loc(key_word, data_list):
    f = open(key_word + '.json', 'r')
    jf = json.load(f)
    for item in jf:
        if item['coordinates']:
            data_list.append(item)
    return data_list


def feed_keywords (out_f):
    data_list = [ ]
    out_f = open(out_f, 'w')
    words_sheet = open('key_words_es.csv')
    reader = csv.DictReader(words_sheet)
    for row in reader:
        key_word = row['Environmental Keywords in Spanish']
        data_list = get_data_with_loc(key_word, data_list)
    json.dump(data_list, out_f)
    return True

if __name__ == "__main__":
    feed_keywords('data_loc.json')

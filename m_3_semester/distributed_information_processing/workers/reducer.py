#!/usr/bin/env python3
import sys


def _stdout_result():
    for _word, item in key_dict.items():
        for _doc_id, _count in item.items():
            print('%s\t%s' % (str(_word) + ',' + str(_doc_id), str(_count)))


def _debug_str(string: str, out: str = './output/debug.txt'):
    with open(out, 'a+') as f:
        f.write(string)


key_dict = {}

for line in sys.stdin:
    (key, count) = line.rstrip().split('\t', 1)
    (word, doc_name) = key.split(',', 1)

    if not key_dict.get(word):
        key_dict[word] = {
            doc_name: count
        }
    else:
        if not key_dict[word].get(doc_name):
            key_dict[word][doc_name] = count
        else:
            key_dict[word][doc_name] += count
_stdout_result()

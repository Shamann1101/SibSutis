#!/usr/bin/env python3
import sys
from math import log


def _stdout_result():
    for _word, item in tf_dict.items():
        for _doc_id, tf_idf in item.items():
            # print('%s\t%s' % (str(_word) + ',' + str(_doc_id), tf_idf))
            print('%s\t%.12f' % (str(_word) + ',' + str(_doc_id), tf_idf))


def _set_tf_dict():
    doc_count = len(set([item for sublist in [list(v.keys()) for v in key_dict.values()] for item in sublist]))
    for _word, d in key_dict.items():
        for _doc_id, _count in d.items():
            c = sum([v[_doc_id] if v.get(_doc_id) else 0 for (w, v) in key_dict.items()])
            tf = int(_count) / c
            idf = log(doc_count / len(key_dict[_word].keys()))
            tf_idf = tf * idf
            # result = f'{_count}/{c}={tf},'
            # result += f'log({doc_count}/{len(key_dict[_word].keys())})={idf},'
            # result += f'{tf}*{idf}={tf_idf}'
            # _debug_str(result + '\n')  # FIXME
            if not tf_dict.get(_word):
                tf_dict[_word] = {_doc_id: tf_idf}
            else:
                tf_dict[_word][_doc_id] = tf_idf


def _debug_str(string: str, out: str = './output/debug.txt'):
    with open(out, 'a+') as f:
        f.write(string)


key_dict = {}  # {word: {doc_id: count}}
tf_dict = {}

for line in sys.stdin:
    (word, value) = line.rstrip().split('\t', 1)
    (doc_id, count) = value.split(',', 1)
    count = int(count)

    if not key_dict.get(word):
        key_dict[word] = {
            doc_id: count
        }
    else:
        if not key_dict[word].get(doc_id):
            key_dict[word][doc_id] = count
        else:
            key_dict[word][doc_id] += count
_set_tf_dict()
_stdout_result()

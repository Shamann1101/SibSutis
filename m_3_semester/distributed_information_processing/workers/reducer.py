#!/usr/bin/env python3
import sys
from math import log


def _stdout_result():
    for _word, item in tf_dict.items():
        for _doc_id, tf_idf in item.items():
            # print('%s\t%s' % (str(_word) + ',' + str(_doc_id), tf_idf))
            print('%s\t%.12f' % (str(_word) + ',' + str(_doc_id), tf_idf))


def _set_doc_dict():
    for _word, d in key_dict.items():
        for _doc_id, _count in d.items():
            if not doc_dict.get(_doc_id):
                doc_dict[_doc_id] = {_word: _count}
            else:
                doc_dict[_doc_id][_word] = _count


def _set_tf_dict():
    for _word, d in key_dict.items():
        for _doc_id, _count in d.items():
            tf = int(_count) / len(list(doc_dict[_doc_id]))
            idf = log(len(doc_dict.keys()) / len(key_dict[_word].keys()))
            tf_idf = tf * idf
            # result = f'{_count}/{len(list(doc_dict[_doc_id]))}={tf},'
            # result += f'log({len(doc_dict.keys())}/{len(key_dict[_word].keys())})={idf},'
            # result += f'{tf}*{idf}={tf_idf}'
            if not tf_dict.get(_word):
                tf_dict[_word] = {_doc_id: tf_idf}
            else:
                tf_dict[_word][_doc_id] = tf_idf


def _debug_str(string: str, out: str = './output/debug.txt'):
    with open(out, 'a+') as f:
        f.write(string)


key_dict = {}  # {word: {doc_id: count}}
doc_dict = {}  # {doc_id: {word: count}}
tf_dict = {}

for line in sys.stdin:
    (key, value) = line.rstrip().split('\t', 1)
    (word, doc_id) = key.split(',', 1)
    (count, word_count) = value.split(',', 1)

    if not key_dict.get(word):
        key_dict[word] = {
            doc_id: count
        }
    else:
        if not key_dict[word].get(doc_id):
            key_dict[word][doc_id] = count
        else:
            key_dict[word][doc_id] += count
_set_doc_dict()
_set_tf_dict()
_stdout_result()

#!/usr/bin/env python3
import re
import sys

re_short_tag = re.compile(r'>?\s*<(?P<tag>\w+)([^<]*?>(?P<payload>[^<]+))?(?(2)</(?P=tag)>|[^<]+/>)')
re_open_tag = re.compile(r'<(?P<tag>\w+)[^>]*?>')
re_close_tag = re.compile(r'</(?P<tag>\w+)>')
TOP_WORDS_LIMIT = 20


def _str_cleanup(string: str) -> str:
    # return str.lower(re.sub(r'\W', '', string))
    return str.lower(string)


def _iterate_line_contents(_word: str, _doc_name: str):
    word = _str_cleanup(_word)
    if word == '':
        return
    key_list.append(word + ',' + _doc_name)

    if not key_dict.get(word):
        key_dict[word] = {
            _doc_name: 1
        }
    else:
        # if not key_dict[word].get(_doc_name):
        if not key_dict[word][_doc_name]:
            # _debug_str(str(key_dict) + '\n')
            key_dict[word][_doc_name] = 1
        else:
            # _debug_str(f'before[{word}]: ' + str(key_dict[word]) + '\n')
            key_dict[word][_doc_name] += 1
            # _debug_str(f'after[{word}]: ' + str(key_dict[word]) + '\n')


def _get_top_words(limit: int = TOP_WORDS_LIMIT) -> list:
    return list(
        dict(sorted((sum([v for v in value.values()]), key) for (key, value) in key_dict.items())[-limit:]).values())


def _stdout_result():
    # for _key in key_list:
    #     print('%s\t%s' % (_key, 1))

    for word, item in key_dict.items():
        if word in _get_top_words():
            continue
        for doc_id, count in item.items():
            print('%s\t%s' % (str(word) + ',' + str(doc_id), str(count)))


def _debug_str(string: str, out: str = './output/debug.txt'):
    with open(out, 'a+') as f:
        f.write(string)


revision = False
text = False
page_id = None
key_list = []
key_dict = {}
for line in sys.stdin:
    if 'revision' in re.findall(re_open_tag, line):
        revision = True
        continue

    if 'revision' in re.findall(re_close_tag, line):
        revision = False
        continue

    if not revision:
        continue

    skip_tag = False
    for m in re.finditer(re_short_tag, line):
        tag = m.group('tag')
        if tag == 'id':
            page_id = m.group('payload')
            skip_tag = True
            continue
        elif tag == 'text':
            revision = False
            skip_tag = True
            continue
    if skip_tag:
        continue

    if 'text' in re.findall(re_open_tag, line):
        text = True
        continue

    if 'text' in re.findall(re_close_tag, line):
        text = False
        page_id = None
        continue

    if not revision or not text or not page_id:
        continue

    line_contents = re.split(r'\W', line)
    if len(line_contents) == 0:
        continue
    for content in line_contents:
        _iterate_line_contents(content, page_id)

_stdout_result()

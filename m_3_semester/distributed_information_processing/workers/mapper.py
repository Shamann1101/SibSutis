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
    print('%s\t%s' % (
        word,
        str(_doc_name) + ',1'
    ))


def _get_top_words(limit: int = TOP_WORDS_LIMIT) -> list:
    return [
        'в', 'и', 'на', 'с', 'по', 'не', 'из', 'что', 'к', 'от', 'года', 'для', 'как', 'а', 'о', 'был', 'за', 'году',
        'его', 'до'
    ][:limit]  # FIXME
    # top_list = list(
    #     dict(sorted((sum([count for count in value.values()]), word) for (word, value) in key_dict.items())[
    #          -limit:]).values())
    # return top_list


def _debug_str(string: str, out: str = './output/debug.txt'):
    with open(out, 'a+') as f:
        f.write(string)


revision = False
contributor = False
text = False
page_id = None
for line in sys.stdin:
    if not revision and 'revision' in re.findall(re_open_tag, line):
        revision = True
        continue

    if revision and 'revision' in re.findall(re_close_tag, line):
        revision = False
        continue

    if not revision:
        continue

    if not contributor and 'contributor' in re.findall(re_open_tag, line):
        contributor = True
        continue

    if contributor and 'contributor' in re.findall(re_close_tag, line):
        contributor = False
        continue

    skip_tag = False
    for m in re.finditer(re_short_tag, line):
        tag = m.group('tag')
        if tag == 'id' and not contributor:
            page_id = m.group('payload')
            skip_tag = True
            continue
        elif tag == 'text':
            revision = False
            skip_tag = True
            continue
    if skip_tag:
        continue

    if not text and 'text' in re.findall(re_open_tag, line):
        text = True
        continue

    if text and 'text' in re.findall(re_close_tag, line):
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

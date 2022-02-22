# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_5_sentence_gen
   Description :   惰性实现
   date：          2022/2/21
-------------------------------------------------
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # ➊
        for match in RE_WORD.finditer(self.text):
            yield match.group()


if __name__ == '__main__':
    s = Sentence('"The time has come,",the Walrus said,')
    print(s)
    for word in s:
        print(word)

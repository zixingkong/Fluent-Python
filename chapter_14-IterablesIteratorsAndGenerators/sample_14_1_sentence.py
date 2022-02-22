# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_14_1_sentence
   Description :   单词序列
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

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
    s = Sentence('"The time has come,",the Walrus said,')
    print(s)
    for word in s:
        print(word)
    print(s[0])
    print(s[5])
    print(s[-1])
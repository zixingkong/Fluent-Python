# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_3.8
   Description :
   date：          2022/2/10
-------------------------------------------------
"""

import collections


class StrKeyDict(collections.UserDict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str[key]]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str[key]] = item

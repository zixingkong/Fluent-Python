# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_17_13_flags2_sequential.py
   Description :
   date：          2022/3/15
-------------------------------------------------
"""
import collections
from http import HTTPStatus

import requests
from tqdm import tqdm

from sample_17_12_flags2_sequential import download_one


def download_many(cc_list, base_url, verbose, max_req):
    counter = collections.Counter()  # ➊
    cc_iter = sorted(cc_list)  # ➋
    if not verbose:
        cc_iter = tqdm.tqdm(cc_iter)  # ➌
    for cc in cc_iter:  # ➍
        try:
            res = download_one(cc, base_url, verbose)  # ➎
        except requests.exceptions.HTTPError as exc:  # ➏
            error_msg = 'HTTP error {res.status_code} - {res.reason}'
            error_msg = error_msg.format(res=exc.response)
        except requests.exceptions.ConnectionError as exc:  # ➐
            error_msg = 'Connection error'
        else:  # ➑
            error_msg = ''
            status = res.status
        if error_msg:
            status = HTTPStatus.error  # ➒
        counter[status] += 1  # ➓
        if verbose and error_msg:
            print('*** Error for {}: {}'.format(cc, error_msg))
    return counter

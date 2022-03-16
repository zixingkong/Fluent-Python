# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_17_12_flags2_sequential.py
   Description :
   date：          2022/3/15
-------------------------------------------------
"""
from http import HTTPStatus

import requests
from flags2_common import save_flag, Result


def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = requests.get(url)
    if resp.status_code != 200:  # ➊
        resp.raise_for_status()
    return resp.content


def download_one(cc, base_url, verbose=False):
    try:
        image = get_flag(base_url, cc)
    except requests.exceptions.HTTPError as exc:  # ➋
        res = exc.response
        if res.status_code == 404:
            status = HTTPStatus.not_found  # ➌
            msg = 'not found'
        else:  # ➍
            raise
    else:
        save_flag(image, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'
    if verbose:  # ➎
        print(cc, msg)
    return Result(status, cc)  # ➏

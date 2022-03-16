# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_17_14_flags2_threadpool.py
   Description :
   date：          2022/3/15
-------------------------------------------------
"""
import collections
from concurrent import futures
import requests
import tqdm  # ➊
from flags2_common import main, HTTPStatus  # ➋
from sample_17_12_flags2_sequential import download_one  # ➌

DEFAULT_CONCUR_REQ = 30  # ➍
MAX_CONCUR_REQ = 1000  # ➎


def download_many(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    with futures.ThreadPoolExecutor(max_workers=concur_req) as executor:  # ➏
        to_do_map = {}  # ➐
        for cc in sorted(cc_list):  # ➑
            future = executor.submit(download_one, cc, base_url, verbose)  # ➒
            to_do_map[future] = cc  # ➓
        done_iter = futures.as_completed(to_do_map)  # 11
        if not verbose:
            done_iter = tqdm.tqdm(done_iter, total=len(cc_list))  # 12
        for future in done_iter:  # 13
            try:
                res = future.result()  # 14
            except requests.exceptions.HTTPError as exc:  # 15
                error_msg = 'HTTP {res.status_code} - {res.reason}'
                error_msg = error_msg.format(res=exc.response)
            except requests.exceptions.ConnectionError as exc:
                error_msg = 'Connection error'
            else:
                error_msg = ''
                status = res.status
            if error_msg:
                status = HTTPStatus.error
            counter[status] += 1
            if verbose and error_msg:
                cc = to_do_map[future]  # 16
                print('*** Error for {}: {}'.format(cc, error_msg))
    return counter


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
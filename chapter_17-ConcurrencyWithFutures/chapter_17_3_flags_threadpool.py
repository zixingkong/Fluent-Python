# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     chapter_17_3_flags_threadpool
   Description :
   date：          2022/3/15
-------------------------------------------------
"""
from concurrent import futures
from sample_17_2_flags import save_flag, get_flag, show, main  # ➊

MAX_WORKERS = 20  # ➋


def download_one(cc):  # ➌
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))  # ➍
    with futures.ThreadPoolExecutor(workers) as executor:  # ➎
        res = executor.map(download_one, sorted(cc_list))  # ➏
    return len(list(res))  # ➐


if __name__ == '__main__':
    main(download_many)  # ➑

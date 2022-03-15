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
    cc_list = cc_list[:5]  # ➊
    with futures.ThreadPoolExecutor(max_workers=3) as executor:  # ➋
        to_do = []
        for cc in sorted(cc_list):  # ➌
            future = executor.submit(download_one, cc)  # ➍
            to_do.append(future)  # ➎
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))  # ➏
        results = []
        for future in futures.as_completed(to_do):  # ➐
            res = future.result()  # ➑
            msg = '{} result: {!r}'
            print(msg.format(future, res))  # ➒
            results.append(res)
    return len(results)


if __name__ == '__main__':
    main(download_many)  # ➑

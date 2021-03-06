# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_18_5_flags_asyncio.py
   Description :
   date：          2022/3/16
-------------------------------------------------
"""

import sys

sys.path.append('../chapter_17-ConcurrencyWithFutures')
import asyncio
import aiohttp
from sample_17_2_flags import BASE_URL, save_flag, show, main


@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    client = aiohttp.ClientSession()
    resp = yield from client.get(url=url)
    image = yield from resp.read()
    return image


@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


if __name__ == '__main__':
    main(download_many)

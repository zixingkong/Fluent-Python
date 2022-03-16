# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     sample_18_8_flags_asyncio
   Description :
   date：          2022/3/16
-------------------------------------------------
"""
# import asyncio
# import collections
#
# from tqdm import tqdm
#
#
# from sample_17_2_flags import BASE_URL, save_flag, show, main
# from sample_17_12_flags2_sequential import download_one
#
#
# @asyncio.coroutine
# def downloader_coro(cc_list, base_url, verbose, concur_req): #➊
#     counter = collections.Counter()
#     semaphore = asyncio.Semaphore(concur_req) #➋
#     to_do = [download_one(cc, base_url, semaphore, verbose)
#     for cc in sorted(cc_list)]: #➌
#         to_do_iter = asyncio.as_completed(to_do) #➍
#         if not verbose:
#         to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list)) #➎
#             for future in to_do_iter: #➏
#             try:
#                 res = yield from future #➐
#             except FetchError as exc: #➑
#                 country_code = exc.country_code# ➒
#                 try:
#                     error_msg = exc.__cause__.args[0] #➓
#                 except IndexError:
#                     error_msg = exc.__cause__.__class__.__name__
#                 if verbose and error_msg:
#                     msg = '*** Error for {}: {}'
#                     print(msg.format(country_code, error_msg))
#                 status = HTTPStatus.error
#             else:
#                 status = res.status
#                 counter[status] += 1
#     return counter
# def download_many(cc_list, base_url, verbose, concur_req):
#     loop = asyncio.get_event_loop()
#     coro = downloader_coro(cc_list, base_url, verbose, concur_req)
#     counts = loop.run_until_complete(coro)
#     loop.close()
#     return counts
# if __name__ == '__main__':
#     main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)
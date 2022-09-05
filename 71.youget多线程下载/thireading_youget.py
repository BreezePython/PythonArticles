import os
import time
import threading
from collections import deque

ERROR_DICT = {}
RETRY_TIME = 5
THREAD_NUM = 30
SEM = threading.Semaphore(THREAD_NUM)


class DownloadThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
        self.name = name
        self.exec_ed = []

    def run(self):
        while download_list:
            url = download_list.popleft()
            print('%s notice: start %s left count: %s' % (self.name, url, len(download_list)))
            SEM.acquire()
            r = os.system(f'you-get -t 600 --no-caption -o {download_path} {url}')
            if r:
                print(f'download error {url}\n')
                ERROR_DICT[url] = ERROR_DICT.get(url, 0) + 1
                if ERROR_DICT[url] <= RETRY_TIME:
                    download_list.append(url)
            else:
                self.exec_ed.append(url)
                time.sleep(0.5)
            SEM.release()
        print('%s notice:Already exec:%s' % (self.name, self.exec_ed))


if __name__ == '__main__':
    download_path = r"E:\Vedio\Java\青空の霞光-Java连载\5.JavaSE9-17新特性"
    download_url = "https://www.bilibili.com/video/BV1tU4y1y7Fg"
    start_num = 1
    count = 19
    page_list = [i for i in range(start_num, start_num + count)]
    download_list = deque()
    for i in page_list:
        download_list.append(f"{download_url}?p=%s" % i)
        # download_list.extend(['xxx'])
    thread_list = []
    for thread_num in range(THREAD_NUM):
        t = DownloadThread(f"download_thread={thread_num}")
        t.start()
        thread_list.append(t)
        time.sleep(0.5)
    for td in thread_list:
        td.join()
    print("download_finish.")
    if ERROR_DICT:
        print(f"error history: {ERROR_DICT}.")
        print(f'final error list:\n'
              f'{[i for i in sorted(ERROR_DICT.keys()) if ERROR_DICT[i] > RETRY_TIME]}')

# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/11/17 23:50:09
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : get_source_code.py

import platform
import os
import time
import shutil


def get_tmp_path():
    if platform.platform().lower().startswith('windows'):
        return os.getenv('temp')
    else:
        return '/tmp'


class GetSourceCode:
    def __init__(self):
        self.base_path = os.path.dirname(__file__)
        self.tmp_path = get_tmp_path()
        self.basic_dirs = self.get_dirs()
        self.code_dir = None

    def get_dirs(self):
        for root, dirs, files in os.walk(self.tmp_path):
            return set(dirs)

    def get_source_dir(self):
        while True:
            _dir = list(self.get_dirs() - self.basic_dirs)
            if _dir and _dir[0].startswith('_MEI'):
                self.code_dir = _dir[0]
                print("find source code dir %s" % self.code_dir)
                break
            else:
                time.sleep(0.2)
        self.copy_code_dir()

    def copy_code_dir(self):
        abs_tmp_path = os.path.join(self.tmp_path, self.code_dir)
        while os.path.exists(abs_tmp_path):
            source_path = os.path.join(self.base_path, self.code_dir)
            if not os.path.exists(source_path):
                os.mkdir(source_path)
            for root, dirs, files in os.walk(abs_tmp_path):
                for file in files:
                    remote_path = root.replace(abs_tmp_path, source_path).replace('\\', '/')
                    if not os.path.exists(remote_path):
                        print(remote_path)
                        os.makedirs(remote_path)
                    if not os.path.exists(remote_path + '/' + file):
                        shutil.copy(os.path.join(root, file), remote_path)
        print("Get source code end.")


if __name__ == '__main__':
    print("start Source Code Analyse project.")
    print("Monitoring source files...")
    g = GetSourceCode()
    g.get_source_dir()

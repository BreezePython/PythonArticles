# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/06/29 22:45:31
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : shutil升级.py
#
# import os
#
# for root, dirs, files in os.walk('D:\\software_temp', topdown=False):
#     for name in files:
#         os.remove(os.path.join(root, name))
#     for name in dirs:
#         os.rmdir(os.path.join(root, name))

# import shutil
# shutil.rmtree('D:\\software_temp')

import pprint
# import shutil
#
# pprint.pprint(shutil.get_unpack_formats())

# import py7zr
#
# def decompress(file):
#     archive = py7zr.Archive(file)
#     archive.extractall(path="/tmp")

from py7zr import pack_7zarchive, unpack_7zarchive
import shutil

# register file format at first.
shutil.register_archive_format('7zip',
                               pack_7zarchive,
                               description='7zip archive')

shutil.register_unpack_format('7zip',
                              ['.7z'],
                              unpack_7zarchive,
                              description='7zip archive')
pprint.pprint(shutil.get_unpack_formats())
# # extraction
# shutil.unpack_archive('test.7z', '/tmp')

# compression
shutil.make_archive('a', '7zip', '.')

# pprint.pprint(shutil.get_unpack_formats())



# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/11/04 22:48:33
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : compare_version.py
import re


class CompareVersion:
    def __init__(self, version_list):
        self.versions = version_list
        self.error_version_num = 0

    def com_version(self, version):
        sum_version = 0
        version_weights = [10000, 100, 1]
        pattern = re.compile(r'^[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}')
        if not pattern.match(version):
            self.error_version_num += 1
            return -1
        version_list = version.split('.')
        for index, small_version in enumerate(version_list):
            sum_version += version_weights[index] * int(small_version)
        return sum_version

    def sort_version(self):
        sorted_version = sorted(self.versions, key=lambda x: self.com_version(x))
        return sorted_version[self.error_version_num:]


if __name__ == '__main__':
    versions = ['0.0.0', '99.99.99', '100.0.1', '1.0.-1', '1.1.99', '2.10.1', '2.9.10', '999', '10-0.1']
    main_class = CompareVersion(versions)
    print(main_class.sort_version())

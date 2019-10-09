# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @Date     : 2019/9/3 0:46
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : PythonYaml.py

import yaml
from yaml.composer import ComposerError


class YamlLoader:
    def __init__(self, file):
        self.file = file

    def load_choice(self):
        with open(self.file, 'r') as f:
            data = f.read()
        try:
            return yaml.safe_load(data)
        except ComposerError:
            return yaml.safe_load_all(data)

    def file_load(self):
        info = self.load_choice()
        print(info)
        if isinstance(info, dict):
            self.file_dump(info, single=True)
        else:
            self.file_dump(info)

    def file_dump(self, data, single=None):
        with open('new_{}'.format(self.file), 'w', encoding='utf-8') as f:
            if single:
                f.write(yaml.safe_dump(data))
            else:
                f.write(yaml.safe_dump_all(data))


yaml_read_single = YamlLoader('breeze_single.yaml')

yaml_read_single.file_load()

yaml_read = YamlLoader('breeze.yaml')

yaml_read.file_load()

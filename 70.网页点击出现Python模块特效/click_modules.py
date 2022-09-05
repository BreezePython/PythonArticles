# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2021/01/09 23:54:47
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : click_modules.py


import sys
# 提供我们将模块列表转化为字符串所需
import json
# from pip._internal.utils.misc import get_installed_distributions
# 过滤掉那些 _开头的C语言链接库
modules = [name for name in sys.modules if not name.startswith('_')]
print(len(modules)) # 53个
# 等待获取完成后再导入pip，否则内置模块编程了177个
from pip._internal.utils.misc import get_installed_distributions
for module_name in get_installed_distributions():
    modules.append(module_name.key)
print(len(modules))  # 还以为自己用了很多，原来全量才135个啊...
print(json.dumps(sorted(modules)))






# print(pip.main("List"))



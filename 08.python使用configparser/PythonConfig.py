# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/8 22.使用Python学习打军体拳:30
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : PythonConfig.py
import configparser

# 初始化
conf = configparser.ConfigParser()
# 读取配置文件
conf.read('config.ini', encoding='utf-8')
# 获得配置文件中的所有sections
print(conf.sections())
# section是区分大小写的，写成小写会被认为不存在
print(conf.has_section('mysql'))
# 获取section = Mysql 下的所有options，即keys
print(conf.options('Mysql'))
# option 不区分大小写，判断结果为True
print(conf.has_option('Mysql', 'DATABASE'))
# 获取section = Mysql 下的所有键值对
print(conf.items('Mysql'))
# 获取section=Mysql下host键对应的value值
# get方法通过不同类型，存在getint、getfloat、getboolean 不同的类型
# 其中getboolean 可以识别 true/false、 1/0、yes/no、 on/off
print(conf.get('Mysql', 'host'))
print(conf.getboolean('Mysql', 'status'))
print(conf.get('Mysql', 'uri'))
# 删除键值对，同样的还设有remove_section(section)就不演示了...
# conf.remove_section('Mysql')
conf.remove_option('Mysql', 'status')


# 我们添加了section为Python，并创建了tools=Pycharm
# 打印显示正常，但是配置文件中，并没有
conf.add_section('Python')
conf.set("Python", "tools", "Pycharm")
print(conf.get("Python", "tools"))
# 此时的配置保存在内存中，需要写入文件方可生效
with open("config.ini", "w+") as f:
    conf.write(f)


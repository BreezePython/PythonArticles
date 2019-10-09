# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/27 23:26
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : LearnPsutil.py


import psutil

for pid in psutil.pids():
    p = psutil.Process(pid)
    print(p.name())
    print(p.as_dict())
    # print()

# print(psutil.boot_time())
# print(datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H: %M: %S"))
# mem = psutil.virtual_memory()
# print(mem)
# print(mem.total/1024/1024)
# print(mem.total)
# print(mem.used)
# print(mem.free)


# # cpu的完整信息
# print(psutil.cpu_times())
# # CPU逻辑个数
# print(psutil.cpu_count())
# # cpu使用率
# print(psutil.cpu_percent())


# disks = psutil.disk_partitions()
# for disk in disks:
#     print(disk.device, psutil.disk_usage(disk.device))

# io = psutil.disk_io_counters()
# print('磁盘IO:', io)
# print('数据类型:', type(io), '\n')

# print(psutil.pids())
#
# for pid in psutil.pids():
#     print(psutil.Process(pid))
#     p = psutil.Process(pid)
#     print(p.name())
#     print(p.as_dict())
# print(p.cmdline())
# print(p.cwd())
# print(p.name())
# # print(p.exe())  # 进程的bin路径
# print(p.cwd())  # 进程的工作目录绝对路径
# print(p.status())  # 进程状态
# print(p.create_time())  # 进程创建时间
# print(p.uids())  # 进程uid信息
# print(p.gids())  # 进程的gid信息
# print(p.cpu_times())  # 进程的cpu时间信息,包括user,system两个cpu信息
# print(p.cpu_affinity())  # get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
# print(p.memory_percent())  # 进程内存利用率
# print(p.memory_info())  # 进程内存rss,vms信息
# print(p.io_counters())  # 进程的IO信息,包括读写IO数字及参数
# p.connectios()  # 返回进程列表
# p.num_threads()  # 进程开启的线程数
# from subprocess import PIPE
#
# p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"], stdout=PIPE)
# p.name()
# p.username()

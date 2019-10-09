# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/27 1:26
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : IpPortCheck.py

import socket

IPs = ['127.0.0.1', '10.45.226.74']
Ports = [22, 80, 8080]

for ip in IPs:
    for port in Ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        result = s.connect_ex((ip, port))
        if result == 0:
            print("The Server IP: {} , Port {} has been used".format(ip, port))
        elif result == 10061:
            print("The Server IP: {} , Port {} not enabled".format(ip, port))
        elif result == 10035:
            print("The Server IP: {} , no response".format(ip, port))
        else:
            print(result)
        s.close()

# TimeoutError: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
# ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。

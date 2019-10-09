# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/9/1 21:44.NationalFlag
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : LearnLogging.py
#
# import logging
# logger = logging.getLogger("simple_example")
# logger.setLevel(logging.DEBUG)
# # create file handler which logs even debug messages
# fh = logging.FileHandler("spam.log")
# fh.setLevel(logging.DEBUG)
# # create console handler with a higher log level
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# # create formatter and add it to the handlers
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
# # add the handlers to logger
# logger.addHandler(ch)
# logger.addHandler(fh)
# # "application" code
# logger.debug("debug message")
# logger.info("info message")
# logger.warning("warn message")
# logger.error("error message")
# logger.critical("critical message")

# import logging
#
# logger.basicConfig(filename='exp.log',
# #                     level=logging.DEBUG,
# #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# #
# #
# logger.debug('This is debug message')
# logger.info('This is info message')
# logger.warning('This is warning message')
# logger.error('This is error message')
# logger.critical('This is critical message')

# import logging
# from logging.handlers import RotatingFileHandler
#
# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.INFO)
# formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
#                               datefmt='%Y-%m-%d %H:%M:%S')
# # handler = logging.FileHandler("log.txt")
# handler = RotatingFileHandler("log.txt", maxBytes=1024*3, backupCount=3)
# handler.setLevel(logging.INFO)
# handler.setFormatter(formatter)
#
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# console.setFormatter(formatter)
#
# logger.addHandler(handler)
# logger.addHandler(console)
#
# for i in range(100):
#     logger.info(i)
#     logger.debug('This is debug message')
#     logger.info('This is info message')
#     logger.warning('This is warning message')
#     logger.error('This is error message')
#     logger.critical('This is critical message')

import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(console)

try:
    1/0
except Exception as error:
    logger.error(error)

    logger.error(error, exc_info=True)

    logger.exception("find exception...")




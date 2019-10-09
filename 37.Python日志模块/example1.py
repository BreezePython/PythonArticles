# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/9/1 22:31
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : example1.py


import logging


class ContextFilter(logging.Filter):
    def filter(self, record):
        record.userid = '123'
        return True


if __name__ == '__main__':
    # create logger
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    # create formatter for console handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to console handler
    ch.setFormatter(formatter)

    # create file handler and set level to warn
    fh = logging.FileHandler('spam.log')
    fh.setLevel(logging.WARN)
    # create formatter for file handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(userid)s - %(message)s')
    # add formatter to file handler
    fh.setFormatter(formatter)
    # add context filter to file handler
    fh.addFilter(ContextFilter())

    # add ch、fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message %s', 'args')
    logger.error('error message')
    logger.critical('critical message')

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("simple_example")
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
# fh = logging.FileHandler("spam.log")
# fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
# fh.setFormatter(formatter)

Rthandler = RotatingFileHandler('span.log', maxBytes=10, backupCount=5)
Rthandler.setLevel(logging.INFO)
formatter1 = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
Rthandler.setFormatter(formatter1)
# add the handlers to logger
logger.addHandler(ch)
# logger.addHandler(fh)
logger.addHandler(Rthandler)
a = 5
b = 0
for x in range(100):
    try:
        c = a / b
    except:
        # logging.error("Exception occurred %s" % e)
        # 下面三种方式三选一，推荐使用第一种
        logger.exception("Exception occurred")
        # logger.error("Exception occurred", exc_info=True)
        # logging.log(level=logging.DEBUG, msg="Exception occurred", exc_info=True)

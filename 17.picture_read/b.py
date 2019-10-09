# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/24 0:25
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : image_show.py


from flask import Flask, render_template
import base64
import requests

app = Flask(__name__)


@app.route("/show")
def show_image():
    r = requests.get('http://img.chebiaow.com/thumb/cb/allimg/1303/1-1303061Z600520,c_fill,h_138,w_160.jpg')
    image = base64.b64encode(r.content).decode('ascii')
    return render_template('index.html', img=image)


if __name__ == '__main__':
    app.run()

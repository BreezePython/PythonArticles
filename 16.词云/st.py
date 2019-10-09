# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/23 23:11
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : st.py

# import wordcloud
#
# w = wordcloud.WordCloud()
# w.generate("python and 123")
# w.to_file("a.png")


# from flask import Flask
# from flask import send_file
# from flask import make_response
# from io import BytesIO
# import requests
#
#
# app = Flask(__name__)
#
#
# @app.route("/show_image")
# def show_image():
#     """从mongodb读取二进制图片数据并显示"""
#
#
#     file_name = "a.png"
#     file_type = "png"
#     r = requests.get('http://img.chebiaow.com/thumb/cb/allimg/1303/1-1303061Z600520,c_fill,h_138,w_160.jpg')
#
#     file_data = r.content  # 读取二进制的图片文件,具体方法略
#     # resp = make_response(send_file(BytesIO(file_data), attachment_filename=file_name, as_attachment=True,
#     #                                mimetype=file_type))
#     resp = make_response(send_file(BytesIO(file_data), attachment_filename=file_name, as_attachment=True,
#                                    mimetype='image/png'))
#     """把文件名的中文从utf-8转成latin-1,这是防止中文的文件名造成的混乱"""
#     resp.headers["Content-Disposition"] = "attachment; filename={}".format(file_name.encode().decode('latin-1'))
#     return resp
#
#
# if __name__ == '__main__':
#     app.run()

import sys
from flask import Flask
import requests
import qrcode
from io import BytesIO
from flask import send_file

app = Flask(__name__)


@app.route("/image")
def test_qrcode():

    qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=1
    )
    qr.add_data("http://segmentfault.com/q/1010000004052685")
    img = qr.make_image()

    byte_io = BytesIO()
    # r = requests.get('http://img.chebiaow.com/thumb/cb/allimg/1303/1-1303061Z600520,c_fill,h_138,w_160.jpg')
    img.save(byte_io, 'PNG')
    byte_io.seek(0)

    return send_file(r.content, mimetype='image/png')


if __name__ == "__main__":

    app.run(host="localhost", port=5000, debug=True)
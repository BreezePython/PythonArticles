# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/10 21:24
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : Enneagram_GUI.py


x = ''
with open('New_千字文.txt', encoding='utf-8') as f:
    data = f.readlines()

for line in data:
    y = '<tr>'
    for i in line.split('，'):
        y += '<td>%s</td>' % i
    x += y

a = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link href="https://cdn.bootcss.com/twitter-bootstrap/3.4.1/css/bootstrap.min.css" rel="stylesheet">
    <title>Document</title>
    <style type="text/css">
    	.container{
    		width: 500px;
    	}
    </style>
</head>
<body>
	<div class="container">
	<table class="table table-striped table-bordered table-hover">
	%s
	</table>
</div>
</body>
</html>
''' % x

print(a)

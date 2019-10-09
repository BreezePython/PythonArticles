# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/21 0:05
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : LearnJson.py

# import json
# a = {'name':'BreezePython','sex':'male','adult':True}
#
# b = json.dumps(a,indent=4)
#
# print(json.loads(b))

# with open('a.txt','w+') as f:
#     f.write('123123123')
#     data = f.read()
#
# print(data)

import json

data = {
    "in_use": True,
    "info": {
        "name_cn": '清风Python',
        "name_en": "BreezePython",
    },
    "contents": ["Python", "Java", "Linux"]

}
json.dumps(data,ensure_ascii=False)

# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, indent=4)
#     # f.write(json.dumps(data, indent=4))

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    # data = json.loads(f.read())
print(data)

#### 博客图床与盗链

上周主要的时间，都用在搭建个人博客上。个人一直是在简书平台上使用markdown发文，在这次的博客文章迁移中，遇到了很多坑，其中最为麻烦的就是文章的图床盗链问题。

现在绝大多数的网站都做了反盗链的防护，导致从简书导出的文章，图片链接全部失效，使我基本处在崩溃边缘。几百张的历史博客图文，难道要一点点搬迁吗？答案当然是否定的，最终通过爬虫的方式解决了600张图片的迁移，并完成博客的正常发布与展示。喜欢的朋友可以去我的博客逛逛。

[我的个人博客: https://qingfengpython.cn](https://qingfengpython.cn)

![个人博客](https://gitee.com/BreezePython/blogimages/raw/master/images//0febb1c0486711eb93c9002b67682234.gif)

还不了解如何搭建个人博客的朋友，可以看看我上一篇文章：

[5分钟教你免费搭建个人博客，并部署上线：https://mp.weixin.qq.com/s/JmzV8eIc_llIizmthlL9gg](https://mp.weixin.qq.com/s/JmzV8eIc_llIizmthlL9gg)

今天，就为大家介绍一下，全网通用的markdown文章，图床搭建、迁移方案与代码实现！

#### markdown插入图片

随着越来越多的人开始使用markdown写作，在对markdown的语法简洁高效而欢喜的同时，却对markdown的图片展示而发愁。如何在markdown中插入图片，相信已经成为很多人的苦恼所在。来看看这篇文章的阅读量就知道了，只是几百字的文章，发文两年阅读量45万。

![image-20201227231002749](https://gitee.com/BreezePython/blogimages/raw/master/images//10e4fdd0486711eb8951002b67682234.png)

那么今天，就教大家如何彻底解决markdown图床问题，并且针对已经在其他平台发布过的markdown文章，给出通用的反盗链图片迁移方式。

#### markdown图片语法

在markdown中，针对图片的语法格式为：

```markdown
![图片链接文字](图片路径)
![image-20201227231002749](https://gitee.com/BreezePython/blogimages/raw/master/images//11553150486711eb9b83002b67682234.png)
![清风Python](https://gitee.com/BreezePython/blogimages/raw/master/images//11b449e8486711eba7b3002b67682234.png)

```

其中图片链接的url，可以是url的链接方式，也可以是保存在本地的目录方式。那么，不管是针对本地的图片还是之前在其他网站，使用网站床图上传的历史图片，我们都可以通过今天的文章来实现自己的床图搭建！

#### 个人床图实现方案

网上那些床图工具七牛云等等，始终不是自己，今天就来教大家完成个人床图的搭建。

首先，我们需要创建一个git仓库，github、或者码云都可以。(推荐后者，访问速度快....）

上次在给大家介绍博客搭建时，模拟创建了一个BlogTest的仓库，其实本人自用的是Blog仓库以及搭配的blogimages仓库。

![image-20201227233311106](https://gitee.com/BreezePython/blogimages/raw/master/images//120d2264486711ebb9c9002b67682234.png)

申请好仓库后，我们在仓库下创建一个images文件夹，上传一张图片，然后开始分析仓库的url，码云和github基本类似:

![image-20201227235214348](https://gitee.com/BreezePython/blogimages/raw/master/images//1291135e486711eb9537002b67682234.png)

大家可以看到，仓库下存储的图片url，和图片展示的url，存在一定的切换逻辑。码云上只是将tree改为了raw，github变更的稍微多一些，但都有迹可循。

那么，我们的图床就可以通过往仓库上传图片的方式来实现了！

#### 本地图床实现

本人日常编写markdown，都是使用**Typora**工具，这里就不多介绍了截个图吧，简单几个字来形容：**用过都说好！**

![image-20201227235534205](https://gitee.com/BreezePython/blogimages/raw/master/images//12e04e9e486711eb8f6a002b67682234.png)

那么，关于本地markdown图传实现方式，我就介绍通过Typora的操作来实现。

1. 我们通过Typora的文件 ==> 偏好设置==>图像，设置插入图片时，复制到制定路径,然后将路径定位到咱们clone到本地的床图仓库images文件夹内。此时我们本地编写markdown时，已经可以通过粘贴的方式自动将图片拷贝至床图仓库地址了。Typora生成的图片路径为：

   `![image-20201227235713536](https://gitee.com/BreezePython/blogimages/raw/master/images/image-20201227235713536.png)`

![image-20201227235713536](https://gitee.com/BreezePython/blogimages/raw/master/images//13ee6f9a486711eb9509002b67682234.png)

2. 当文章写完后，我们将markdown进行全文替换：

   ```
   比如，初始链接：
   https://gitee.com/BreezePython/blogimages/raw/master/images/image-20201227235713536.png
   我们将：https://gitee.com/BreezePython/blogimages/raw/master/images/
   替换为仓库的图片展示地址：
   https://gitee.com/BreezePython/blogimages/raw/master/images/
   ```

3. 然后使用 git add 、 git commit 、git push 三连击，将仓库下本次通过Typora添加的图片上传至仓库，即可完成博客床图的生成与展示，是不是很方便呢？

#### 历史图片爬虫迁移

笔者在简书，存在200多篇的历史博文，所有文章共计涉及到将近600张图片的迁移，如果手动操作，我需要：

1. 逐篇文章打开，检索图片链接字段
2. 拷贝图片的链接信息
3. 粘贴至浏览器
4. 下载该图片，并设置图片uuid名称。
5. 保存至床图仓库
6. 修改历史文章内部的图片url链接
7. 最终完成文章保存于图片上传仓库操作

如果这么手动操作，给我一个月都弄不完，估计最终电脑都可能比我气得摔了。所以手动操作自然是行不通的，那么如果通过代码来实现呢？只要50行，连编码，带迁移，半个小时的时间足够了。来说说具体实现吧....

其实代码只是把上面的手工操作，使用文件读写、正则匹配、爬虫下载的方式实现而已，其中比较绕的就是正则了，有一句话这么说：

> 当一件事情遇到了正则，那么它就变成了两件事...

#### 正则遇到的坑

首先，通过正则判断哪些是图片，这个还算比较简单：

`re.compile('!\[.*\]\(https://.*(png|jpg|gif)')`

比对markdown的格式，叹号开头、中括号包含图片说明、小括号涵盖url链接。ok吗？看着没问题，然后第一次迁移发现只有200多张图片....错在哪里？

![image-20201228001606744](https://gitee.com/BreezePython/blogimages/raw/master/images//1440d7f8486711eb9322002b67682234.png)

很多时候我们的图片，尤其是通过Typora来编写的markdown，在图片前面都会添加一段空白，导致最终匹配错误...**所以我们需要在正则的开头，添加 `\s*` 用来匹配一个或者多个空白字符。**

 解决了这个问题，我又遇到了新的情况：

`![文章被锁定](https://upload-images.jianshu.io/upload_images/5847426-00e191420386f54c.gif?imageMogr2/auto-orient/strip)`

简书的url链接是上面这样的，我在下载后，需要进一步的匹配判断问号等情况的匹配。

根据url使用requests进行图片下载，这里由于是床图，网站是不会添加cookie等限制的，直接无脑下载即可。

图片下载好后，我们需要使用uuid库，为我们的图片创建唯一识别码。当然你也可以向Typora那样使用毫秒级别的时间戳，看个人爱好。

最终代码如下：

```python
# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/12/28 23:53:52
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : download_images.py
import os
import re
import uuid
import requests


class DownloadImages:
    def __init__(self, file_path, git_image_path, expects):
        self.file_path = file_path
        self.remote_path = git_image_path
        self.expect_dict = expects

    def read_file(self):
        for root, dirs, files in os.walk(self.file_path):
            if os.path.split(root)[-1] in self.expect_dict.get('dirs'):
                continue
            for file in files:
                if file in self.expect_dict.get('files'):
                    continue
                self.analysis_url(os.path.join(root, file))

    def analysis_url(self, file):
        file_info_list = list()
        with open(file, 'r', encoding='utf-8') as f:
            data = f.readlines()
        for line in data:
            markdown_pattern = re.compile('\s*!\[.*\]\(https://.*(png|jpg|gif)')
            if markdown_pattern.match(line):
                url_pattern = re.compile('https://.*(png|jpg|gif)')
                url = url_pattern.search(line)[0]
                git_url = self.download(url)
                file_info_list.append(re.sub('https://.*(png|jpg|gif).*', git_url+')', line))
            else:
                file_info_list.append(line)
        with open(file, 'w', encoding='utf-8') as f:
            f.writelines(file_info_list)

    def download(self, url):
        print(url)
        image_type = url.split('.')[-1]
        image_name = '%s.%s' % (uuid.uuid1().hex, image_type)
        image_path = os.path.join(self.remote_path, image_name)
        response = requests.get(url)
        img = response.content
        with open(image_path, 'wb') as f:
            f.write(img)
        return 'https://gitee.com/BreezePython/blogimages/raw/master/images/%s' % image_name


if __name__ == '__main__':
    markdown_path = r'D:\blog\markdown'
    remote_path = r'D:\blogimages\images'
    expect_dict = {"dirs": ['.git', '.idea', 'static'],
                   "files": ["README.md", "_sidebar.md"]}
    main = DownloadImages(markdown_path, remote_path, expect_dict)
    main.read_file()
```

最终，572张历史markdown图片迁移成功

![image-20201228002613832](https://gitee.com/BreezePython/blogimages/raw/master/images//14b07578486711eb9154002b67682234.png)

最后的最后，把本地仓库下的图片一股脑上传到码云、github上即可。

上面的代码适配了例外路径和文件，针对码云仓库拿来即用，只需要简单修改下你的本次仓库、目录和url前缀即可！

#### 个人博客的重要性

之前的文章已经强调过了，坚持写博客不论是对知识积累巩固与面试加分上都占有举足轻重的地位，个人博客的免费搭建、历史博文的迁移、日常markdown博客的床图，这些都帮大家捋顺了，你还有什么理由不开始坚持学习与总结呢？

今天的文章就到这里，码字不易，觉得有收获还望点赞支持。好东西要用来分享，欢迎转发文章给你身边同样需要它的朋友。
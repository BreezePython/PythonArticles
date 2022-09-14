> 今天来和大家聊聊日常经常使用到的偷懒方法 --> **defaultdict**

## defaultdict示例

字典作为日常使用频率较高的一种数据类型，常会遇到判断key是否在字典中的情况。

这时，我们是否按照如下代码写的：

```python
d = dict()
if 'key' in d:
    d['key'] += 1
else:
    d['key'] = 0
print(d['key']) # 1
```

我们每次都需要判断后再进行相关操作。

但是，当我们使用了defaultdict后，就可以偷懒的简化if else 的格式了：

```python
from collections import defaultdict

d = defaultdict(int)
d["key"] += 1
print(d['key']) # 1
```

## 关于defaultdict

大家日常使用到defaultdict的场景，绝大多数都是上述举例为了减少if else的判断。

当然除了默认的int初始化，还有列表追加 `d = defaultdict(list)` 的无脑append操作。

可是，我们是否有深挖过defaultdict的其他场景呢？来先看看它的源码：

```python
    def __init__(self, default_factory=None, **kwargs): 
        # known case of _collections.defaultdict.__init__
        """
        defaultdict(default_factory=None, /, [...]) --> 
        dict with default factory
        
        The default factory is called without arguments to produce
        a new value when a key is not present, in __getitem__ only.
        A defaultdict compares equal to a dict with the same items.
        All remaining arguments are treated the same as if they were
        passed to the dict constructor, including keyword arguments.
        
        # (copied from class doc)
        """
        pass
```

源码注释中，只是简单说明了使用default_factory参数，可以让调用键不存在时生成新值。

就比如我们上面 `defaultdict(int)` 将key不存在时，value默认赋值0， `d = defaultdict(list)`  将key不存在时，value默认赋值空列表。

听起来功能就是如此了吧...

现在我们来换个场景，拿同学们打力扣周赛举个例子。

## 力扣周赛

每个人参加力扣周赛时，会根据我们的比赛结果进行评分。如果是第一次参加比赛，因为没有初始积分，从0分开始不太合适。

所以每位选手的初始基准分为1500分。这样就可以根据选手分数来考量本次比赛表现进行加分了。

先来看看默认字典的代码应该如何操作：

```python
scores = dict()
add_score = 10
# 方法1
if 'xiaoming' in scores:
    scores['xiaoming'] += add_score
else:
    scores['xiaoming'] = 1500 + add_score

# 方法2
scores['xiaoming'] = scores.get('xiaoming', 1500) + add_score
```

现在我们想使用defaultdict，但defaultdict如果赋值int，就没办法提供这个基准分了，该如何是好？

此时我们应该深入理解下 **default_factory** ，它不仅仅支持我们传入默认的int、list，还支持我们使用自定义函数。

```python
from collections import defaultdict

def diy_func():
    print("init user score.")
    return 1500

scores = defaultdict(diy_func)
scores['xiaoming'] += 10
print(scores['xiaoming'])
# init user score.
# 1510
```

我们通过自定义一个函数赋值给  **default_factory**， 帮我们初始化用户的分数。

但这个自定义的函数方法有些太过单一了，是否可以简化？此时我们应该考虑到lambda表达式啊！

```python
scores = defaultdict(lambda: 1500)
scores['xiaoming'] += 10
print(scores['xiaoming'])
```

这样做是不是就更简洁方便了。有没有觉得这操作很nice？

然而，我们注意到defaultdict的 `__init__` 方法是存在 `**kwargs**` 参数，我们还没有使用呢！

它还可以这么玩：

```python
from collections import defaultdict

data = defaultdict(xiaozhang=1600, xiaowang=1700)

scores = defaultdict(lambda: 1500, data)
scores['xiaoming'] += 10
scores['xiaowang'] -= 15
print(scores.items())
# dict_items([('xiaozhang', 1600), ('xiaowang', 1685), ('xiaoming', 1510)])
```

所以，defaultdcit可以在 使用 **default_factory** 的基础上，导入初始的字典进行。是不更溜了？

关于default_dict的内容，今天就学到这里吧，希望对大家有所帮助。


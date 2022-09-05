## 锲子

> 在Python开发的过程中，我们经常使用到.sort()和sorted()方法，但你知道这两者使用的差别么？
>
> 在文章的开始，我来提出几个问题考考大家，看看大家对下面6个问题是否都清楚、明白。

1.  sorted()可以排序字符串么 ？ 比如 sorted('adbc')  

2. .sort()方法是否可以作用于集合与字典？

3. `arr = [('a', 1), ('b', 5), ('a', 3), ('b', 4)]` 如何按照列表元素的字符升序和数字降序进行排列？

4. 什么叫做 **stable** 稳定排序？

5. 对上述arr列表，以下四种排序的结果一样么？

   ```python
   arr = [('a', 1), ('b', 4), ('a', 2), ('b', 3)]
   # 第一种
   print(sorted(arr, key=lambda x: [x[0], -x[1]]))
   # 第二种
   print(sorted(sorted(arr, key=lambda x: x[0]), key=lambda x: -x[1]))
   # 第三种
   arr.sort(key=lambda x: [x[0], -x[1]])
   print(arr)
   # 第四种
   arr.sort(key=lambda x: x[0])
   arr.sort(key=lambda x: -x[1])
   print(arr)
   ```

6. 你是否了解 **cmp_to_key** 方法的使用 ？



## sort和sorted的介绍

今天我来带大家，深入了解 .sort()和sorted()方法，有哪些不为人知的细节！

首先，我们来看看Python代码中，这两个方法的注释和所处的位置。

以下内容，来自Python源码：

```python
# sort
class list(object):   
    def sort(self, *args, **kwargs): # real signature unknown
        """
        Sort the list in ascending order and return None.
        
        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
        order of two equal elements is maintained).
        
        If a key function is given, apply it once to each list item and sort them,
        ascending or descending, according to their function values.
        
        The reverse flag can be set to sort in descending order.
        """
        pass
    
# sorted
def sorted(*args, **kwargs): # real signature unknown
    """
    Return a new list containing all items from the iterable in ascending order.
    
    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    """
    pass
```

通过源码注释以及日常使用的经验，可以总结一下表格：

| 场景         | .sort()      | sorted                                     |
| ------------ | ------------ | ------------------------------------------ |
| 默认排序形式 | 升序         | 升序                                       |
| 支持参数     | key、reverse | key、reverse                               |
| 可使用对象   | list         | iterable（str、list、couple、set、dict...) |
| 排序方式     | 原地排序     | 创建排序后的列表                           |
| 返回值       | None         | 排序后的list                               |

对于上面的表格，解释为：

1. .sort()和sorted都默认以升序进行排序，并且支持reverse和key 两个参数。
2. .sort()是list类的方法，所以只能针对列表进行排序；而sorted可以面向任何**可迭代对象**进行排序。在使用范围上sorted()使用范围更广。
3. .sort()执行时，针对当前列表进行原地排序；而sorted则会创建一个新列表，将可迭代对象排序后，保存在这个新的列表中。（str也是可迭代对象哦！）
4. .sort()由于是原地排序，故此没有返回值；而sorted将可迭代对象排序后保存在一个新的列表中，作为返回值。

## 常规操作

> 让我们通过以下几个例子先来熟悉下他们的基础操作吧。

### 默认排序

```python
# 默认排序
arr = [1, 5, 3, 2, 4]
b = sorted(arr)
print(b)
# 返回排序后的新列表 [1, 2, 3, 4, 5]
print(arr)
# sorted 不会修改原列表 [1, 5, 3, 2, 4]
print(sorted(arr, reverse=True))
# 生成一个逆序的列表 [5, 4, 3, 2, 1]
print(arr.sort())
# 原地排序，无返回值 None
print(arr)
# sort 修改了原始的列表 [1, 2, 3, 4, 5]
arr.sort(reverse=True)
print(arr)
# 将原始列表逆序排列  [5, 4, 3, 2, 1]

```

### 使用key的条件排序

```python
# 对列表中的元祖，针对场景进行排序
# 1. 对字符串升序排列
arr = [('a', 1), ('b', 5), ('a', 3), ('b', 4)]
print(sorted(arr, key=lambda x: x[0]))
# [('a', 1), ('a', 3), ('b', 5), ('b', 4)]
arr.sort(key=lambda x: x[0])
print(arr)
# [('a', 1), ('a', 3), ('b', 5), ('b', 4)]

# 2. 对字符串降序排列
arr = [('a', 1), ('b', 5), ('a', 3), ('b', 4)]
print(sorted(arr, key=lambda x: -ord(x[0])))
# [('b', 5), ('b', 4), ('a', 1), ('a', 3)]
arr.sort(key=lambda x: -ord(x[0]))
print(arr)
# [('b', 5), ('b', 4), ('a', 1), ('a', 3)]

# 3. 对数字降序排序
arr = [('a', 1), ('b', 5), ('a', 3), ('b', 4)]
print(sorted(arr, key=lambda x: -x[1]))
# [('b', 5), ('b', 4), ('a', 3), ('a', 1)]
arr.sort(key=lambda x: -x[1])
print(arr)
# [('b', 5), ('b', 4), ('a', 3), ('a', 1)]

# 4. 结合1、2,先对字符串升序，再对数字降序
arr = [('a', 1), ('b', 5), ('a', 3), ('b', 4)]
print(sorted(arr, key=lambda x: [x[0], -x[1]]))
# [('a', 3), ('a', 1), ('b', 5), ('b', 4)]
arr.sort(key=lambda x: [x[0], -x[1]])
print(arr)
# [('a', 3), ('a', 1), ('b', 5), ('b', 4)]

```

**总结：** 

1. 针对字符串的排序时，采用按位比较的方式，即针对字符串下标从零开始逐个比较。
2. 对于降序，如果是数字将整数变为负数即可，但对于单个的字符，则需要将其转化为ascii码
3. 当多个条件时，可以通过列表的方式，条件组装起来。

## 面试风骚知识点

> 通过上面的基础学习，.sort()和sorted()的基础使用方式已经有所了解了。
>
> 下面来回答开篇的第五个问题。四种排序的结果是否一致。

先来揭晓答案：

```python
arr = [('a', 1), ('b', 4), ('a', 2), ('b', 3)]
# 第一种
print(sorted(arr, key=lambda x: [x[0], -x[1]]))
# 第二种
print(sorted(sorted(arr, key=lambda x: x[0]), key=lambda x: -x[1]))
# 第三种
arr.sort(key=lambda x: [x[0], -x[1]])
print(arr)
# 第四种
arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: -x[1])
print(arr)
# 1、3的结果是：
# [('a', 2), ('a', 1), ('b', 4), ('b', 3)]
# 2、4的结果是：
# [('b', 4), ('b', 3), ('a', 2), ('a', 1)]
```

- 1、3的条件放在一个列表里面，表示是需要同时成立的。

- 2、4将两个条件拆分开，指在表达先排序一次，再排序一次，前后两者**没有必然的联系**。

注意我将没有必然联系几个字加粗了，那么，真的是没有必然联系么？ 当然不是的！

这就引出了开篇提到的，**稳定排序**。

请看下面的例子：

```python
arr = [('d', 1), ('a', 1), ('c', 2), ('b', 2)]
print(sorted(arr, key=lambda x: -x[1]))
# [('c', 2), ('b', 2), ('d', 1), ('a', 1)]
print(sorted(arr, key=lambda x: x[1]))
# [('d', 1), ('a', 1), ('c', 2), ('b', 2)]
```

大家可以看到，不管我们对数字进行正序还是逆序操作，在数字相同的情况下，d的位置都要前于a，c的位置都要前于b。

正如sort源码中说到：

  `stable (i.e. the order of two equal elements is maintained).` 保持两个相等元素的顺序。

## cmp_to_key

最后的最后，我们还差一个问题： 你是否了解 **cmp_to_key** 方法的使用？

通过上面众多例子，我们掌握了.sort()和sorted中key关键字的妙用，它可以通过lambda的方式，让我们实现很多自定义的排序。

但lambda的初衷，是为了完成匿名函数简洁、快速使用方式。

有时候的排序规则较为繁琐，这时候我们该怎么做呢？

我们可以通过 **cmp_to_key**，对sorted的key进行扩展。

让我们看一道力扣真题。



## [179.最大数](https://leetcode.cn/problems/largest-number/solution/179zui-da-shu-pythonshuang-jie-by-qingfe-ijnw/)

> https://leetcode.cn/problems/largest-number/solution/179zui-da-shu-pythonshuang-jie-by-qingfe-ijnw/
>
> 难度：中等

## 题目：

给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

提示：
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 10 ^ 9

## 示例：
```
示例 1：
输入：nums = [10,2]
输出："210"

示例2：
输入：nums = [3,30,34,5,9]
输出："9534330"

示例 3：
输入：nums = [1]
输出："1"

示例 4：
输入：nums = [10]
输出："10"
```

## 分析

这里首先需要注意的一点，当用例为全零数组时，我们需要返回ret[0]

由于这道题nums.length<=100，所以第一时间考虑的使用冒泡排序的法子。

之前就做过类似题目，了解可以通过cmp_to_key的方法弥补sorted方法中， key使用lambda匿名函数存在的不足。 

所以通过cmp_to_key也可以巧妙解决这个问题。

## 解题1 冒泡排序：

```python
class Solution:
    def largestNumber(self, nums):
        ret = ''
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]
            ret += str(nums[i])
        ret += str(nums[-1])
        return ret[0] if int(ret) == 0 else ret
```

## 解题2 cmp_to_key：

```python
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        def cmp(a, b):
            return 1 if a + b >= b + a else -1

        ret = sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True)
        return ''.join(ret) if ret[0] != '0' else '0'
```



今天给大家针对.sort()和sorted()的进行了细致的讲解，学到这里再回顾看开篇的几个问题，检查下自己学习的成果吧。

欢迎大家将自己的心得，在留言区进行分享与讨论，今天的内容就到这里了，感谢大家的支持。

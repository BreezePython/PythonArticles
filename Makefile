> 子在川上曰，逝者如斯夫，不舍昼夜...一个不小心，中秋节的三天小长假就耗尽了！

## 关于周赛

放假错过了力扣周赛，回头看题目时，震惊于周赛第三题的不摇碧莲。

最近很多人吐槽，力扣周赛的题目越来越不走心，这次周赛第三题就更过分了，直接使VIP的原题改了几个字发出来充数。

这是逼着大家全去充值VIP的节奏么？

## 白嫖VIP

最近力扣在准备秋季赛，报名地址：

[https://leetcode.cn/contest/season/2022-fall/](https://leetcode.cn/contest/season/2022-fall/)

点击报名个人赛和战队赛后，就可以通过能量，换取5天的VIP兑换码。
![在这里插入图片描述](https://img-blog.csdnimg.cn/479dad92a1ba4e5a9ad0f4093267cfcb.png)


说重点：今年的礼品兑换BUG又出现了，可以使用小号获得VIP兑换码，然后给自己正在使用的号码充值。也就是说注册一个号就能白嫖5天的VIP，发挥大家的人际关系网，白嫖它一个月都不成问题。



## [2406.将区间分为最少组数](https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/)

> https://leetcode.cn/problems/divide-intervals-into-minimum-number-of-groups/
>
> 难度：中等

### 题目

给你一个二维整数数组 intervals ，其中 intervals[i] = [lefti, righti] 表示 闭 区间 [lefti, righti] 。
你需要将 intervals 划分为一个或者多个区间 组 ，每个区间 只 属于一个组，且同一个组中任意两个区间 不相交 。
请你返回 最少 需要划分成多少个组。
如果两个区间覆盖的范围有重叠（即至少有一个公共数字），那么我们称这两个区间是 相交 的。比方说区间 [1, 5] 和 [5, 8] 相交。 

提示：
- 1 <= intervals.length <= 10 ^ 5 
- intervals[i].length == 2 
- 1 <= lefti <= righti <= 10 ^ 6

### 示例

```
示例 1：
输入：intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
输出：3
解释：我们可以将区间划分为如下的区间组：
- 第 1 组：[1, 5] ，[6, 8] 。
- 第 2 组：[2, 3] ，[5, 10] 。
- 第 3 组：[1, 10] 。
可以证明无法将区间划分为少于 3 个组。

示例 2：
输入：intervals = [[1,3],[5,6],[8,10],[11,13]]
输出：1
解释：所有区间互不相交，所以我们可以把它们全部放在一个组内。
```

### 分析

先来吐槽下，看看VIP的253题：

![](https://img-blog.csdnimg.cn/b7dcb681910d4c0faaacd84a1e645336.png)


遇到数组题，我们第一时间考虑的就是要不要排序。
显然这道题希望我们返回不重叠且最少划分的组个数，所以我们应该按照子数组的index[0]进行排序。
这里，我们可以考虑维护一个优先队列(小顶堆)：
- 当堆顶数字小于当前子数组的左边界数字时，修改堆顶数字为子数组的右边界
- 当堆顶数字大于当前子数组的左边界数字时，堆内无满足条件的区间，需要新插入子数组的右边界

由于数组时排序的，所以当子数组同时满足对个条件时，直接插入堆顶即可，而无需具体到邻近的那个值。

对于Python的朋友可以关注下，在第一种情况时，无需弹出堆顶，再插入子数组的右边界。这样会造成堆的二次排序。
可以使用heapreplace的方法，直接完成堆顶的排序即可。具体可以看下源码注释：
```python
def heapreplace(heap, item):
    """Pop and return the current smallest value, and add the new item.

    This is more efficient than heappop() followed by heappush(), and can be
    more appropriate when using a fixed-size heap.  Note that the value
    returned may be larger than item!  That constrains reasonable uses of
    this routine unless written as part of a conditional replacement:

        if item > heap[0]:
            item = heapreplace(heap, item)
    """
```

### 解题

**Python:**

```python
import heapq
class Solution:
    def minGroups(self, intervals):
        intervals.sort()
        hq = []
        for l, r in intervals:
            if not hq or hq[0] >= l:
                heapq.heappush(hq, r)
            else:
                heapq.heapreplace(hq, r)
        return len(hq)
```

**Java:**

```java
class Solution {
    public int minGroups(int[][] intervals) {
        Arrays.sort(intervals, (x, y) -> x[0] - y[0]);
        PriorityQueue<Integer> q = new PriorityQueue<Integer>();
        for (int[] interval : intervals) {
            if (!q.isEmpty() && q.peek() < interval[0]) {
                q.poll();
            }
            q.offer(interval[1]);
        }
        return q.size();
    }
}
```


欢迎关注我的公_众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

我的个人博客：https://qingfengpython.cn

力扣解题合集：https://github.com/BreezePython/AlgorithmMarkdown

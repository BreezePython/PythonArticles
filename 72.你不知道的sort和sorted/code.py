### 默认排序 ###
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

print("=" * 100)

### 使用key的条件排序 ###

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

print("=" * 100)

### 第五个问题 ###
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

print("=" * 100)

### 稳定排序 ###
arr = [('d', 1), ('a', 1), ('c', 2), ('b', 2)]
print(sorted(arr, key=lambda x: -x[1]))
# [('c', 2), ('b', 2), ('d', 1), ('a', 1)]
print(sorted(arr, key=lambda x: x[1]))
# [('d', 1), ('a', 1), ('c', 2), ('b', 2)]

print("=" * 100)



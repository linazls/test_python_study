# print(1 or 3)
# print(1 and 3)
# print(0 and 2 and 1)
# print(0 and 2 or 1)
# print(0 and 2 or 1 or 4)
# print(0 or False and 1)


# 先and后or
# a or b  # (a为True,右侧短路，返回左侧)
# a and b # (a为False,右侧短路，返回左侧)
# 0为false
name = 'wupeiqi'
print(name[len(name)-1:0:-1]+name[0])   # 字符串切片，前开后闭，需要拼接第一个元素

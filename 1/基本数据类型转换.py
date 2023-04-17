# 基本数值类型：int-整数型， str-字符串， float-浮点型，bool-布尔型
# 1.str（），函数，将数据转换成字符串
intl = 10000
print(intl,type(intl))
stl = str(intl)
print(stl, type(stl))
# 将float（），转换成int型
IT = 2.3
tt = int(IT)
print(tt, type(tt))
# 将布尔型bool（），转化成浮点型float（）
aa = True
bb = float(aa)
print(bb, type(bb))
# 将整数型int（），转化为布尔型bool（）
cc = 28
dd = bool(cc)
print(dd, type(dd))
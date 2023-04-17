# 变量赋值
# 1. 给单个变量进行赋值，使用 =：赋值符号
#  == ：判断左右两边相等
# 使用连等号
x = z = y = 100
print(x, z, y)
o = p = q = "海绵宝宝"
print(o, p, q, "海绵宝宝",)
q = "貂蝉"
w = "王昭君"
r = "甄姬"
q, w, r = w, r, q
print(q, w, r)

fa = False
i4 = float(fa)
print(i4, type(i4))

id = True
print(int(id), type(id))

f1 = 0
print(bool(f1))

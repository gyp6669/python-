# 格式化输出
# 格式化字符串
# 输出到文件中，open（）：打开一个文件，第一个参数是文件名字，第二参数是操作文件方式，w:write 写入
filel = open("data.txt", "w")
print("明天没有课", file=filel)
# %s: 占位符,可以拼接字符串新数据，拼接数据前判断是否为字符串，不是字符串就转换数据类型，str（）
name = "擎天柱"
print("汽车人首领：%s" % name)
number = 1946739379
print("我的电话号码是：%s" % number)
age = 19
school = "河艺"
print("%s, 年龄%s, 学校:%s" %(name, age, school))
# %6.3: 里面的6表示拼接的字符串所占位，。3表示取拼接的字符串前三个，如果站的位置不够，会自动变成与字符串本身长度一样的位置
word = "abcedaidhskdh"
print("%s" % word)
print("%.3s" % word)
print("%6.3s" % word)
print(len(word))
# print("拼接字符串：%d % sl")
# %02d：整数型字符串数据拼接， 里面0表示在数位不够2的时候前面添加0,2表示占两个位置，当数值大于位置的时候，按数字的长度占位
year = 2002
month = 6
day = 1
print("我的生日：%d-%d-%d" % (year, month, day))
print("我的生日：%d-%02d-%02d" % (year, month, day))
# %f 浮点型数据拼接
fi = 12.31
print("%f" % fi)

# 用+号拼接
print("1234"+"475")
name = "杜甫"
hao = "草堂居士"
print(name + hao)
book = "钢铁是怎样炼成的"
publish_year = 1933
price = 26.3
print("书名：%s, 出版日期：%d, 价格：%2f" % (book, publish_year, price))
# 使用format（），函数拼接字符,在拼接的位置写{}
# 1."{}".format()
print("{} - {} - {}".format(book, publish_year, price))
print("{0} - {1} - {2}".format(book, publish_year, price))
print("{pub} - {book} - {price}".format(pub=publish_year, book=book, price=price))
# 特别简单的用法,在字符串前边添加f，{}直接写变量
print(f"{book} {publish_year} {price}")
# %x ， %o 拼接16进制，8进制
# print():打印输出
# 1}输出变量或常量


# 每次print都会换行，这是有一个参数：end， 默认为end= “\n"
# \n:换行符，让字符串在这个地方另起一行
print("我们一起嗨！\n起来嗨", end="!!!")
print("好嗨哟")
"""
\n 这种前边带\后面跟字母或数字，叫做转义字符
\会见后面的字母或数字一起转义，赋予其他意义
\t 制表符，相当于一个tab键
\\ 表示\，使用\取消\转义效果
"""
# print("\")
# len（）：计算字符串长度
print(len(" \ "))
print("\\")
print(len("\\"))
print("机油精\\t关云长\\t小后盾\\t程咬金")
print("橘右京\t典韦a\t甄姬a\t后裔a")
# 字符串前面加r也可以让字符串中的转义字符不再转义
print(r"姓名：黄总\n年龄：66\n性别：男")
# input（）：输入函数，接收来自键盘输入的内容，数据类型是字符串
# name =input（"宝，你叫神魔名字："）
# print(name)
number = input("请输入您的余额：")
number = int(number)
print(number, type(number))




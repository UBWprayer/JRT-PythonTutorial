# 字符串

print('JRT')
print("JRT")  # 字符串来说，单引号和双引号没有区别
print("I'm learning Python")  # 于是不通过麻烦的转义，可以在字符串中适度的使用引号
print('He said:"JRT is short for JLU robot team"')
print('I said: "I\'m learning "')  # 字符串里同时包含了两种引号，该转义还是要转义
print(repr("JRT"))  # repr()返回字符串对机器友好的形式(合法)
print(str("JRT"))  # str()返回字符串对用户有好的形式，print()便调用了str()
print("D:\development\new")  # 没得到你想要的结果，是不是？
print(r'D:\development\new')  # 你想使用的转义字符是可以的，但是Python额外提供了原生字符串
print("""\
         Hello,
         World!""")  # 三引号的字符串也是存在的，该字符串会保留格式，行尾部的\用于忽略换行(续行)
print(''''\
         Hello,
         World!''')  # 三个单引号和三个双引号仍然没有本质区别
print("字符串""拼接")
print('J''R''T')
print("把我输出两遍 "+"把我输出两遍 ")
print("想不想把我输出十遍？ "*10)
string = "JLU robot team"
print(string[0]+'='+string[-0])
print(string[1])  # 字符串下标从0开始
print(string[-1])  # 负索引从字符串末尾开始
print(string[0:-1])  # 切片，包含第一个索引对应的字符，不包含最后一个索引字符
print(string[:])
i = int(input("输入一个整数"))
print(string[:i]+string[i:])  # 这样总是会选取整体，下标越界无所谓，Python会把越界下标解释为数组长度
print(string[0:len(string)])  # 内置函数len()返回字符串长度
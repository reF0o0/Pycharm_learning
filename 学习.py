# 这是一个示例 Python 脚本。
from cmath import acos
from unicodedata import name


# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

#字面量
#int
888
#float
13.14
#string
"坚持"
print("-------------------------------------------------")

#print输出
print(888)
print(13.14)
print("坚持")
print("Stick to it, and you\'ll succeed")
print("坚\n持")
print("""落魄谷中寒风吹，春秋蝉鸣少年归。

荡魂山处石人泪，定仙游走魔向北。

逆流河上万仙退，爱情不敌坚持泪。

宿命天成命中败，仙尊悔而我不悔。""")
num1=666
print("胡一樊"+str(num1))
print("胡一樊",num1)
print("-------------------------------------------------")

#注释
#单行注释
"""
多
行
注
释
"""
print("-------------------------------------------------")

#计算
print(1+2-2*4/2**2+1**3)
import math
print(math.pi)
print(math.e)
print(math.sin(30))
print(math.sin(math.radians(30)))
print(math.log2(4))
print(2**10)
print(math.pow(2,10))
print(math.pow(1024,1/10))
print(math.sqrt(4))
x = 3.7
print(math.ceil(x))      # 向上取整
print(math.floor(x))     # 向下取整
print(round(x))          # 四舍五入
a=-1
b=-2
c=3
print((-b+math.sqrt(b**2-4*a*c))/(2*a))
deta=math.pow(b,2)-4*a*c
print((-b-math.pow(deta,1/2))/(2*a))
print("-------------------------------------------------")

#变量
money = 50
print("中午十二点钱包还有",money,"元")
money = money - 10
print("买了冰淇凌花费 10 元，还剩",money,"元")
print("下午一点，钱包还剩",money,"元")
print("买了巧克力花费 10 元")
money = money - 10
print("下午二点，钱包还剩",money,"元")
print("买了可乐花费 5 元")
money = money - 5
print("下午三点，钱包还剩",money,"元")
print("-------------------------------------------------")

#数据类型
print(type(888))
print(type(13.14))
print(type("坚持"))
print(type(money))
int_type = type(888)
float_type = type(13.14)
string_type = type("坚持")
print(int_type)
print(float_type)
print(string_type)
name = "坚持"
name_type = type(name)
print(name_type)
print("-------------------------------------------------")

#转换
int_str = str(11)
print(type(int_str))
print(int_str)
float_str = str(1.1)
print(type(float_str))
print(float_str)
str_int = int("1")
print(type(str_int))
print(str_int)
str_float = float("1.11")
print(type(str_float))
print(str_float)
float_int = int(2.2)
print(type(float_int))
print(float_int)
int_float = float(2)
print(type(int_float))
print(int_float)
print("-------------------------------------------------")

#len
print(len("Hi!"))
print(len(" 6 "))
print(len("坚\n持"))
print(len("坚\"持"))
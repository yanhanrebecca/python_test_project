"""
九进制正整数2022转换成十进制等于多少？答案：1478
"""


def base_conversion(n):
    # int(x,base),int() 函数用于将一个字符串或数字转换为10进制整型,而base一般代表x的进制
    n = int(n, 9)
    return n


if __name__ == '__main__':
    num = input()
    print(base_conversion(num))

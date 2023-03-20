"""
    题目描述：小蓝要和朋友合作开发一个时间显示的网站。在服务器上，朋友已经获取了当前的时间，用一个整数表示，值为从
    1970 年 1 月 1 日00:00:00到当前时刻经过的毫秒数。现在，小蓝要在客户端显示出这个时间。小蓝不用显示出年月日，
    只需要显示出时分秒即可，毫秒也不用显示，直接舍去即可。给定一个用整数表示的时间，请将这个时间对应的时分秒输出。
    输入：输入一行包含一个整数，表示时间。例子：46800999
    输出：输出时分秒表示的当前时间，格式形如 HH:MM:SS，其中 HH 表示时（取值：[0, 23]），MM 表示分（取值：[0,
    59]），SS 表示秒（取值：[0, 59]）。时、分、秒 不足两位时补前导0。例子：13:00:00
"""
import datetime
def cal_time(ms):
    start = datetime.datetime(year=1970, month=1, day=1)
    #dela是一毫秒
    dela = datetime.timedelta(milliseconds=1)
    #起始时间加上经过的毫秒
    ms = start + ms * dela
    print('%02d:%02d:%02d' % (ms.hour, ms.minute, ms.second))

if __name__ == '__main__':
    now = int(input())
    cal_time(now)
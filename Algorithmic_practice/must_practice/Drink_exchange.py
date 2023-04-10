"""
题目描述:乐羊羊饮料厂正在举办一次促销优惠活动。乐羊羊 C 型饮料，凭 3 个瓶盖可以再换一瓶 C 型饮料，并且可以一直循环下去(但不允许暂借或赊账)。
请你计算一下，如果小明不浪费瓶盖，尽量地参加活动，那么，对于他初始买入的 n 瓶饮料，最后他一共能喝到多少瓶饮料。
输入描述:输入一个整数n
输出描述:输出一个整数，表示实际得到的饮料数。
https://www.lanqiao.cn/problems/143/learning/
"""

cap_sum = int(input())
bottle = cap_sum
while True:
    if cap_sum < 3:
        break
    cap_sum = cap_sum - 3 + 1
    bottle += 1
print(bottle)

"""
https://www.lanqiao.cn/problems/1460/learning/
"""
import math


# 求最小公倍数
def lcm(a, b):
    return a * b / math.gcd(a, b)


dp = []
dp = [float('inf')] * (2021+1)
dp[1] = 0
for i in range(1, 2022):
    for j in range(i + 1, min(i + 22, 2022)):
        if j > 2021:
            break
        dp[j] = min(dp[j], dp[i] + lcm(i, j))
print(dp[2021])

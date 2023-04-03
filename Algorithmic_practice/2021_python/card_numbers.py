"""
https://www.lanqiao.cn/problems/1443/learning/
"""


h = {}
n = 2021
for i in range(10):
    h[str(i)] = n
flag = True
i = 0
while flag:
    i += 1
    for s in str(i):
        h[s] -= 1
        if h[s] < 0:
            flag = False
            break
print(i - 1)

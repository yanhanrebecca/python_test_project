"""
https://www.lanqiao.cn/problems/1463/learning/
"""


n = 2021041820210418
docker = set()
sum = 0
for i in range(1, int(n ** 0.5 + 1)):
    if n % i == 0:
        docker.add(i)
        docker.add(n // i)
for i in docker:
    for j in docker:
        for k in docker:
            if i * j * k == n:
                sum += 1
print(sum)

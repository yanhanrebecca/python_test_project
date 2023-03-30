"""
小明对数位中含有 2、0、1、9 的数字很感兴趣（不包括前导 0），在 1 到 40 中这样的数包括 1、2、9、10 至 32、39 和 40，
共 28 个，他们的和是 574。请问，在 1 到 n 中，所有这样的数的和是多少？
输入描述:输入一行包含一个整数.eg:40
输出描述:输出一行，包含一个整数，表示满足条件的数的和。eg:574
https://www.lanqiao.cn/problems/191/learning/?problem_list_id=6&page=1&sort=students_count
"""
n = int(input())
sum = 0
for i in range(1, n + 1):
    for c in str(i):
        if c in '2019':
            sum += i
            break
print(sum)
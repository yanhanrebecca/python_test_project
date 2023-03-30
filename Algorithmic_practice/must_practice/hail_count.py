"""
https://www.lanqiao.cn/problems/128/learning/?problem_list_id=6&page=1&sort=students_count
"""
n = int(input())
num_list = []
for i in range(n + 1):
    list = []
    max_1 = i
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i = i * 3 + 1
        list.append(n)
    if list:
        m = max(list)
        num_list.append(m)
max = max(num_list)
print(max)


"""
https://www.lanqiao.cn/problems/172/learning/?problem_list_id=6&page=1&sort=students_count
"""
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
i, k = 0, 0
sum = 0
for j in range(n):
    while i < n and a[i] < b[j]:
        i += 1
    while k < n and c[k] >= b[j]:
        k += 1
    sum = i * (n - k)
print(sum)

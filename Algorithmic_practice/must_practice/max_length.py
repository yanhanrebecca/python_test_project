"""
https://www.lanqiao.cn/problems/158/learning/
"""
n = int(input())
a = list(map(int, input().split()))
max_length = 1
for i in range(n):
  length = 1
  for j in range(i + 1, n):
    if a[j] <= a[j - 1]:
      break
    if a[j] > a[j - 1]:
      length += 1
  if length > max_length:
    max_length = length
print(max_length)
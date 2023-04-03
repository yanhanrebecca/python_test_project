"""
https://www.lanqiao.cn/problems/212/learning/
"""


def find_sum(num_list_length, num_list):
    print(num_list)
    sum = 0
    for i in range(num_list_length):
        max = num_list[i]
        min = num_list[i]
        for j in range(i, n):
            if num_list[j] > max:
                max = num_list[j]
            if num_list[j] < min:
                min = num_list[j]
            if max - min == j - i:
                sum += 1
    print(sum)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    find_sum(n, arr)

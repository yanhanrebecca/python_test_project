"""
https://www.lanqiao.cn/problems/1449/learning/
"""


point_list = []
for x in range(20):
    for y in range(21):
        point_list.append([x, y])
print(len(point_list))
result = set()
for i in range(len(point_list)):
    x_1 = point_list[i][0]
    y_1 = point_list[i][1]
    for j in range(len(point_list)):
        x_2 = point_list[j][0]
        y_2 = point_list[j][1]
        if x_2 == x_1:
            continue
        k = (y_2 - y_1) / (x_2 - x_1)
        b = (x_2 * y_1 - x_1 * y_2) / (x_2 - x_1)
        if (k, b) not in result:
            result.add((k, b))
print(len(result) + 20)



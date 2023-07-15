original_list = [1, 2, 3, [4, 5]]
sliced_list = original_list[:]

# 修改切片列表中的元素
sliced_list[0] = 6

# 修改切片列表中的子列表元素
sliced_list[3][0] = 7

print(id(original_list[3]))
print(id(sliced_list[3]))
print(original_list)  # 输出: [1, 2, 3, [7, 5]]
print(sliced_list)  # 输出: [6, 2, 3, [7, 5]]
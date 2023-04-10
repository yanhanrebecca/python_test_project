"""
将ipv4地址转换为ipv6映射地址
"""
ipv4_address = input().split('.')
ipv6_address = '0:0:0:0:0:FFFF:'
temp_list = []
for num in ipv4_address:
    b = hex(int(num)).lstrip('0').strip('x')
    if len(b) == 1:
        b = '0' + b
    temp_list.append(b)
ipv6_mapped_address = ipv6_address + temp_list[0] + temp_list[1] + ':' + temp_list[2] + temp_list[3]
print(ipv6_mapped_address)
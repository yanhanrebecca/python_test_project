"""
将ipv4地址转换为ipv6兼容地址
"""
ipv4_address = input().split('.')
ipv6_address_list = ['0', '0', '0', '0', '0', '0']
for num in ipv4_address:
    b = hex(int(num)).lstrip('0').strip('x')
    ipv6_address_list.append(b)
ipv6_compatible_address = ":".join(ipv6_address_list)
print(ipv6_compatible_address)

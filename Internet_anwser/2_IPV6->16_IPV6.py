"""
将二进制ipv6地址转换为冒号十六进制表示的ipv6地址
"""
ipv6_2_address = input().split(':')
ipv6_16_address_list = []
for num in ipv6_2_address:
    b = hex(int(num)).lstrip('0').strip('x')
    if len(b) != 4:
        b = '0' * (4 - len(b)) + b
    ipv6_16_address_list.append(b)
ipv6_16_address = ":".join(ipv6_16_address_list)
print(ipv6_16_address)
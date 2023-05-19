s = input()
c_list = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up_list = ['A','B','C','D','E','F','G','H','I','G','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
str_list = list(s)
str_list_without = []
for c in str_list:
    if c in c_list:
        str_list_without.append(c)
    if c in up_list:
        str_list_without.append(c.lower())
    if c == ' ':
        continue
print(str_list_without)
if str_list_without == str_list_without[::-1]:
    print("true")
else:
    print("false")

#A man, a plan, a canal: Panama
k = ''

for i in range(125):
    k+='1'

print(k)
while "111" in k:
    k = k.replace("111", "22",1)
    k = k.replace("222","11",1)


print(k, len(k), k.count('1'))

# 121 112 3 2

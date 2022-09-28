# 셀프넘버
result = list(range(1, 10001))
add_list = []

for j in result:
    add_list.append(j+sum([int(k) for k in str(j)]))

add_list = set(add_list)
result = set(result)
self_num = sorted(result - add_list)
print(*self_num, sep='\n')

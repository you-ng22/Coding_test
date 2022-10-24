a, b, v = map(int, input().split())

# day = 0
# height = 0

# while True:
#     day += 1
#     height += 1
#     if height == v:
#         print(day)
#         break
#     height -= b

x = (v-b)/(a-b)
if x == int(x):
    print(int(x))
else:
    print(int(x) + 1)
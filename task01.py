my_tuple = (5, 2, 6, 3, 8, 1)
#my_tuple = (5, 2, 6, 3, "2", 8, 1)

flag = True
for el in my_tuple:
    if type(el) != int:
        flag = False
        break

if flag:
    print(sorted(my_tuple))
else:
    print(my_tuple)
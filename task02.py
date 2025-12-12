import random as rnd

my_tuple = tuple(rnd.randint(0, 9) for i in range(10))
obj = rnd.randint(0, 9)

count = my_tuple.count(obj)
print(my_tuple, obj)

if count == 0:
    print(())
elif count == 1:
    start = my_tuple.index(obj)
    print(my_tuple[start:])
else:
    start = my_tuple.index(obj)
    end = my_tuple.index(obj, start + 1)
    print(my_tuple[start:end + 1])
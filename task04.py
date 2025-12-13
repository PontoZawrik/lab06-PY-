import random as rnd

my_tuple = tuple(rnd.randint(0, 9) for i in range(10))
obj = rnd.randint(0, 9)
print(my_tuple, obj)

result = []
if obj in my_tuple:
    result = list(my_tuple)
    result.remove(obj)
    print(tuple(result))
else:
    print(my_tuple)

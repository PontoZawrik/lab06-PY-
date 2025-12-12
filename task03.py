import random as rnd

my_tuple = tuple(rnd.randint(0, 9) for i in range(10))
print(my_tuple)

unique = set()
result = []

for el in reversed(my_tuple):
    if el not in unique:
        unique.add(el)
        result.append(el)

result = tuple(result)
print(result)
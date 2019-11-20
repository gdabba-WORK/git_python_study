numbers = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 4, 5, 6]
square = []

for i in numbers2:
    square.append(i ** 2)
print(square)

print()
square = [i ** 2 for i in numbers]
print(square)


print()
square = []
for i in numbers:
    if i >= 3:
        square.append(i ** 2)
print(square)


print()
square = [i ** 2 for i in numbers if i >= 3]
print(square)
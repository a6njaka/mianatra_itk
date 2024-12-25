n = 0
for i in range(0, 11):
    for j in range(0, 11):
        print(f"{i} + {j} = {i + j}")
        n += 1

print(f"Total = {n}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

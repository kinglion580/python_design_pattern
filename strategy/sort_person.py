class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def __str__(self):
        return self.name


class ICompare:
    def comparable(self, person1, person2):
        pass


class CompareByAge(ICompare):
    def comparable(self, person1, person2):
        return person1.age - person2.age


personList = [
    Person('Tom', 22, 70, 180),
    Person('Bob', 18, 42, 166),
    Person('Jenny', 32, 52, 175)
]

n = len(personList)
for i in range(0, n-1):
    if CompareByAge().comparable(personList[i], personList[i+1]) > 0:
        tmp = personList[i]
        personList[i] = personList[i+1]
        personList[i+1] = tmp
    i += 1

for p in personList:
    print(p)





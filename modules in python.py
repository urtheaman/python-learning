import random

x = random.randint(0,10)
print(x)

y = random.random() * 1000
print(f"{y:.2f}")
i = 1000
list2 = []
while i>0:
    list1 = ["Ram", "Shyam", "Shivam", "Harry", "John"]
    choice = random.choice(list1)
    list2.append(choice)
    i -= 1
print(list2)
print(list2.count("Ram"))
print(list2.count("Shyam"))
print(list2.count("Shivam"))
print(list2.count("Harry"))
print(list2.count("John"))


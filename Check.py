tuple1 = ['Aman', 1,2,3,3,3,3,4,3]
tuple2 = (1,2,3,3,3,3,4,3)
# print(tuple1.__contains__("Aman"))                                True
# print(tuple2.__contains__("man"))                                 False
# print(tuple1.count(3))                                            5
# print(tuple2.count(3))                                            5
# print(tuple2.index(4))                                            7
# print(tuple1.index(4))                                            7
# print(tuple1.__add__(["The",25,50]))                              ['Aman', 1, 2, 3, 3, 3, 3, 4, 3, 'The', 25, 50]
# print(tuple2.__add__(("The",25,50)))                              ('Aman', 1, 2, 3, 3, 3, 3, 4, 3, 'The', 25, 50)
# print(tuple2.__class__)                                           <class 'tuple'>
# print(tuple1.__class__)                                           <class 'list'>
# print(sorted(tuple2))                                             It Can be Sorted Only If Integers Are Available in the tuple


# print(tuple1)
# print(tuple2)

# x = frozenset({"apple", "banana", "cherry"})
# y = {"apple", "banana", "cherry"}
#
# print(x)
# print(y)
# x.__reduce__()
# y.__reduce__()

# print(x)
# print(y)

# def add(a,b):
#     """Hello"""
#     print("The Sum Is", a+b)
#     return add

# for i in range(0,6,2):
#     print(i)


# print(add.__doc__)

# dict1 = {"Ram": "India", "Age": 28, 28: 56, 28: 56}
# print(dict1)
#
"""Set"""

# fruits = {'apple','Banana', 'Mango'}
# fruits.remove('apple')
# fruits.update({4,25,52,'Aman'})
# fruits.add(258.85)
# print(fruits)
# print(frozenset(fruits))
# print(fruits)

"""FrozenSet"""

# fruits2 = frozenset({'Apple',25,25, 'Banana', 'Cherry'})
# print(set(fruits2))
# print(fruits2)

# list1 = ['aman',2,5,7,9]
# print('aman' in list1)

# x= 3 + 2J
# print(type(x))
for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )


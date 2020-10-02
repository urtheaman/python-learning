# Problem Without Args And Kwargs -
    # we were unable to make scalable applications
    # as shown in the below example we cannot add/print
    # 6th element bcoz the function takes only 5 arguments.

# def cl(a,b,c,d,e):
#     return a,b,c,d,e
#
# x = cl('Ram','Shyam',25,'Aman','Kumar', 'John')
# print(x)

# def fun(*args):
#     # print(args[0])
#     for i in args:
#         print(i)
#     return fun
# a = ['Ram','Shyam',25,'Aman','Kumar', 'John']
# fun(*a)

def fun(normal, *argsharry, **kwargssachin):
    for i in argsharry:
        print(i)
    for item, value in kwargssachin.items():
        print(f"{item} Is {value}")
    return fun
kw = {"Rohan": "Chef", "Harry": "Tutor", "Yaghmare": "Physicist", "Einstein": "Great Physicist"}
a = ['Ram','Shyam',25,'Aman','Kumar', 'John']

fun(*a, **kw)

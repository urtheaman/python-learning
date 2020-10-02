# i = 8 # Global Variable
# def fun(n):
#     i = 6 # Local Variable
#     i += 5
#     print(i, n, "Printed")
#     return n
#
# fun(7)


# # Error
# i = 8 # Global Variable
# def fun(n):
#     i += 5
#     print(i, n, "Printed")
#     return n
#
# fun(7)
# print(i)


# i = 8 # Global Variable
# def fun(n):
#     global i
#     i += 5
#     print(i, n, "Printed")
#     return n
#
# fun(7)
# print(i)


# Nested Functions
x = 89
def Harry():
    x = 20
    def rohan():
        global x
        x = 88
        # print("Before calling Rohan", x)

    print("Before calling Rohan", x)
    rohan()
    print("Harry X is ", x)
Harry()
print(x)


